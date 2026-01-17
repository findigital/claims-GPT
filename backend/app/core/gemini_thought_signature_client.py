"""
Gemini Chat Completion Client with thought_signature support
Intercepts raw HTTP responses to capture and preserve thought_signature
"""

import json
import logging
from typing import Any, Dict, Literal, Mapping, Optional, Sequence

import httpx
from autogen_core import CancellationToken
from autogen_core.models import CreateResult, LLMMessage
from autogen_core.tools import Tool, ToolSchema
from autogen_ext.models.openai import BaseOpenAIChatCompletionClient
from openai import AsyncOpenAI
from pydantic import BaseModel

from app.core.config import settings

logger = logging.getLogger(__name__)


class ThoughtSignatureHTTPClient(httpx.AsyncClient):
    """
    Custom HTTP client that intercepts responses to extract thought_signature.

    Gemini returns thought_signature in: tool_calls[].extra_content.google.thought_signature
    The OpenAI SDK discards extra_content, so we need to capture it here.
    """

    def __init__(self, signature_store: Dict[str, Any], *args, **kwargs):
        """
        Initialize with a reference to the signature store.

        Args:
            signature_store: Dictionary to store extracted thought signatures
        """
        super().__init__(*args, **kwargs)
        self._signature_store = signature_store

    async def send(self, request, *args, **kwargs):
        """Override send to intercept requests AND responses."""

        # STEP 1: Intercept outgoing request to inject thought_signature
        if (
            "chat/completions" in str(request.url)
            and request.method == "POST"
        ):
            try:
                # Read the content stream completely
                content_bytes = b''
                if hasattr(request, 'stream'):
                    async for chunk in request.stream:
                        content_bytes += chunk
                elif hasattr(request, 'content'):
                    content_bytes = request.content
                else:
                    # No content to modify
                    logger.warning("[ThoughtSignatureHTTPClient] Request has no content or stream")

                if content_bytes:
                    # Parse the request body
                    request_data = json.loads(content_bytes)

                    logger.info(f"[ThoughtSignatureHTTPClient] Intercepting outgoing request")

                    # Check if any assistant messages have tool_calls
                    messages = request_data.get("messages", [])
                    modified = False

                    for message in messages:
                        if message.get("role") == "assistant" and "tool_calls" in message:
                            tool_calls = message["tool_calls"]

                            for tool_call in tool_calls:
                                call_id = tool_call.get("id")

                                # Check if we have a stored signature for this call_id
                                if call_id and call_id in self._signature_store:
                                    signature = self._signature_store[call_id]

                                    # Inject thought_signature into tool_call
                                    if "extra_content" not in tool_call:
                                        tool_call["extra_content"] = {}
                                    if "google" not in tool_call["extra_content"]:
                                        tool_call["extra_content"]["google"] = {}

                                    tool_call["extra_content"]["google"]["thought_signature"] = signature

                                    logger.info(
                                        f"[ThoughtSignatureHTTPClient] Injected thought_signature into call_id: {call_id}"
                                    )
                                    logger.info(f"[ThoughtSignatureHTTPClient] Signature: {signature[:50]}...")
                                    modified = True

                    # If we modified the request, create a new request with updated content
                    if modified:
                        new_content = json.dumps(request_data).encode('utf-8')

                        # Create a completely new request object
                        request = httpx.Request(
                            method=request.method,
                            url=request.url,
                            headers={
                                k: v for k, v in request.headers.items()
                                if k.lower() not in ['content-length', 'transfer-encoding']
                            },
                            content=new_content,
                        )
                        logger.info(f"[ThoughtSignatureHTTPClient] Modified request with thought_signature")

            except Exception as e:
                logger.warning(f"[ThoughtSignatureHTTPClient] Error injecting thought_signature: {e}")
                import traceback
                traceback.print_exc()

        # STEP 2: Send the request (possibly modified)
        response = await super().send(request, *args, **kwargs)

        # STEP 3: Intercept incoming response to extract thought_signature
        if (
            response.status_code == 200
            and "chat/completions" in str(request.url)
            and request.method == "POST"
        ):
            try:
                # Parse the response body
                data = json.loads(response.text)

                logger.info(f"[ThoughtSignatureHTTPClient] Intercepted response")

                # Extract thought_signature from each tool call
                if "choices" in data:
                    for choice in data["choices"]:
                        message = choice.get("message", {})
                        tool_calls = message.get("tool_calls", [])

                        for tool_call in tool_calls:
                            # Check for extra_content.google.thought_signature
                            extra_content = tool_call.get("extra_content", {})
                            google_data = extra_content.get("google", {})
                            thought_sig = google_data.get("thought_signature")

                            if thought_sig:
                                call_id = tool_call.get("id")
                                if call_id:
                                    logger.info(
                                        f"[ThoughtSignatureHTTPClient] Found thought_signature for call_id: {call_id}"
                                    )
                                    logger.info(f"[ThoughtSignatureHTTPClient] Signature: {thought_sig[:50]}...")
                                    self._signature_store[call_id] = thought_sig

            except Exception as e:
                logger.warning(f"[ThoughtSignatureHTTPClient] Error extracting thought_signature: {e}")

        return response


class GeminiThoughtSignatureClient(BaseOpenAIChatCompletionClient):
    """
    Gemini client that captures and preserves thought_signature for function calling.

    IMPLEMENTATION:
    1. Uses custom HTTP client to intercept responses
    2. Extracts thought_signature from tool_calls[].extra_content.google.thought_signature
    3. Stores signatures mapped by function call ID
    4. Injects signatures back into requests when sending function results

    Based on Gemini documentation:
    https://ai.google.dev/gemini-api/docs/thought-signatures
    """

    def __init__(
        self,
        model: Optional[str] = None,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 64000,
        **kwargs,
    ):
        """
        Initialize Gemini client with thought_signature capture.

        Args:
            model: Model name (defaults to settings.GEMINI_MODEL)
            api_key: API key (defaults to settings.GEMINI_MODEL)
            base_url: Base URL (defaults to settings.GEMINI_API_BASE_URL)
            temperature: Sampling temperature
            max_tokens: Maximum output tokens (Gemini-3 Flash: 64K)
            **kwargs: Additional arguments passed to parent
        """
        # Use settings if not provided
        model = model or settings.GEMINI_MODEL
        api_key = api_key or settings.GEMINI_API_KEY
        base_url = base_url or settings.GEMINI_API_BASE_URL

        logger.info(f"[GeminiThoughtSignatureClient] Initializing with model: {model}")
        logger.info(f"[GeminiThoughtSignatureClient] Base URL: {base_url}")

        # Store thought signatures: {call_id: thought_signature}
        self._thought_signatures: Dict[str, str] = {}

        # Create custom HTTP client that intercepts responses
        http_client = ThoughtSignatureHTTPClient(
            signature_store=self._thought_signatures,
            timeout=httpx.Timeout(60.0, connect=10.0),
        )

        # Create AsyncOpenAI client with our custom HTTP client
        client = AsyncOpenAI(
            api_key=api_key,
            base_url=base_url,
            http_client=http_client,
        )

        # Define model capabilities for Gemini-3 Flash
        from autogen_core.models import ModelInfo

        model_info = ModelInfo(
            vision=True,
            function_calling=True,
            json_output=True,
            family="unknown",
            structured_output=True,
        )

        # Prepare create args
        create_args = {
            "model": model,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "parallel_tool_calls": False,  # Sequential execution only
        }

        # Initialize parent class
        super().__init__(
            client=client,
            create_args=create_args,
            model_info=model_info,
            **kwargs
        )

        logger.info("[GeminiThoughtSignatureClient] Initialization complete")

    async def create(
        self,
        messages: Sequence[LLMMessage],
        *,
        tools: Sequence[Tool | ToolSchema] = [],
        tool_choice: Tool | Literal["auto", "required", "none"] = "auto",
        json_output: bool | type[BaseModel] | None = None,
        extra_create_args: Mapping[str, Any] = {},
        cancellation_token: CancellationToken | None = None,
    ) -> CreateResult:
        """
        Create completion with thought_signature capture and injection.

        The custom HTTP client will automatically capture thought_signature from responses.
        This method checks if we need to inject thought_signature into the request.

        Args:
            messages: Sequence of messages
            tools: Available tools
            tool_choice: Tool selection mode
            json_output: Whether to use JSON output
            extra_create_args: Extra arguments
            cancellation_token: Cancellation token

        Returns:
            CreateResult with the model's response
        """
        logger.info(f"[GeminiThoughtSignatureClient] create() called with {len(messages)} messages, {len(tools)} tools")

        # Log message types and check for function calls that need thought_signature
        for i, msg in enumerate(messages):
            msg_type = type(msg).__name__
            logger.info(f"[GeminiThoughtSignatureClient] Message {i}: {msg_type}")

            # If AssistantMessage has function calls, check our store
            if msg_type == "AssistantMessage" and hasattr(msg, 'content') and isinstance(msg.content, list):
                for item in msg.content:
                    if hasattr(item, 'id'):
                        call_id = item.id
                        stored_sig = self._thought_signatures.get(call_id)
                        if stored_sig:
                            logger.info(f"[GeminiThoughtSignatureClient]   Call ID {call_id}: Has signature (length: {len(stored_sig)})")
                        else:
                            logger.warning(f"[GeminiThoughtSignatureClient]   Call ID {call_id}: NO signature found!")

        try:
            logger.info(f"[GeminiThoughtSignatureClient] Calling parent create()")

            # NOTE: The parent create() will use our custom HTTP client
            # which will automatically capture thought_signature from the response

            result = await super().create(
                messages=messages,
                tools=tools,
                tool_choice=tool_choice,
                json_output=json_output,
                extra_create_args=extra_create_args,
                cancellation_token=cancellation_token,
            )

            logger.info(f"[GeminiThoughtSignatureClient] Received result")

            # Log captured signatures
            if self._thought_signatures:
                logger.info(f"[GeminiThoughtSignatureClient] Total signatures stored: {len(self._thought_signatures)}")

            return result

        except Exception as e:
            error_msg = str(e)
            logger.error(f"[GeminiThoughtSignatureClient] Error occurred: {error_msg}")

            if "thought_signature" in error_msg:
                logger.error("=" * 80)
                logger.error("[GeminiThoughtSignatureClient] THOUGHT_SIGNATURE ERROR")
                logger.error("=" * 80)
                logger.error(f"Number of messages: {len(messages)}")
                logger.error(f"Number of tools: {len(tools)}")
                logger.error(f"Signatures in store: {len(self._thought_signatures)}")
                logger.error(f"Store keys: {list(self._thought_signatures.keys())}")
                logger.error("=" * 80)

                # The error says thought_signature is missing at "position 2"
                # Position 2 = the AssistantMessage with the function call
                # We need to inject the signature into that message before sending

            raise
