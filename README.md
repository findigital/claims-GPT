# DaveLovable

<div align="center">

**The Most Advanced Open-Source AI Web Development Platform**

*Build React applications at lightning speed with AI-powered multi-agent orchestration*

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![React](https://img.shields.io/badge/React-18.3-61dafb.svg)](https://react.dev)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.8-3178c6.svg)](https://www.typescriptlang.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688.svg)](https://fastapi.tiangolo.com)
[![AutoGen](https://img.shields.io/badge/AutoGen-0.7-orange.svg)](https://microsoft.github.io/autogen)

[Features](#-key-features) • [Demo](#-screenshots) • [Getting Started](#-quick-start) • [Architecture](#-architecture) • [Documentation](#-documentation)

</div>

---

## 🚀 What is DaveLovable?

**DaveLovable** is an open-source AI-powered web development platform inspired by [Lovable.dev](https://lovable.dev), [v0 by Vercel](https://v0.dev), and [Stitch by Google Labs](https://labs.google/stitch). It combines cutting-edge AI orchestration with browser-based execution to deliver the most advanced open-source alternative for rapid frontend prototyping.

Unlike other tools, DaveLovable leverages:
- **Multi-agent AI orchestration** (Microsoft AutoGen 0.7) with 40+ tools
- **Google Gemini-3 Flash Preview** (1M input tokens, 64K output) for blazing-fast code generation
- **WebContainers** (StackBlitz) for true Node.js runtime in the browser
- **Visual editor mode** with click-to-edit and drag-to-adjust controls
- **Full Git version control** with LLM-generated commit messages
- **Real-time streaming** of agent thought processes

**Focus:** Frontend-only development (React + TypeScript + Tailwind CSS). No backend code generation.

---

## ✨ Key Features

### 🤖 **Multi-Agent AI System**
- **2 Specialized Agents:**
  - **Planner Agent**: Strategic coordinator that breaks down tasks and orchestrates execution
  - **Coder Agent**: Execution powerhouse with 40+ tools (file ops, git, terminal, Wikipedia, web search)
- **Smart Routing:** Custom selector automatically routes messages based on context
- **Visual Edit Mode:** Direct routing for CSS/style changes (`[VISUAL EDIT]` tag)
- **Bug Fix Mode:** Direct routing for error fixes (`[BUG FIX]` tag)
- **Parallel Tool Calling:** Create up to 5 files in a single response
- **State Persistence:** Agent conversation history saved per project (survives restarts)

### ⚡ **Gemini-3 Flash Optimization**
- **1M Input Tokens:** Massive context window for complex projects
- **64K Output Tokens:** Generate large files without truncation
- **Custom Thought Signature Client:** Solves Gemini's OpenAI compatibility limitations
- **HTTP-Level Interception:** Preserves reasoning signatures during function calling
- **First Message Optimization:** Provides full file structure upfront, enabling parallel execution

### 🎨 **Visual Editor (Webflow/Framer-style)**
- **Click-to-Edit:** Select elements directly in the preview
- **Live Style Panel:**
  - Colors: Text color, background (color picker with presets)
  - Typography: Font size, weight, alignment
  - Spacing: Drag-to-adjust margin/padding (Shift/Alt modifiers)
  - Border: Width, style, color
  - Effects: Border radius, box shadow, opacity
  - Advanced: Direct className editing
- **Drag Input Component:** Click-and-drag to adjust spacing values
- **AST-Powered Edits:** Surgical code modifications using Python's `ast` module
- **AI Integration:** Send natural language style requests to agents

### 🌐 **WebContainer Integration**
- **True Node.js in Browser:** Full npm + Vite + React environment (powered by StackBlitz)
- **Zero Backend Compute:** All preview runs client-side (infinite scalability)
- **Hot Module Replacement (HMR):** Live code updates without refresh
- **Optimized Loading:**
  - Parallel container boot + file fetch
  - Dependency caching (30-second first load, 5-second after)
  - Incremental file syncing (only changed files)
- **Screenshot Capture:** html2canvas-based DOM capture from inside WebContainer

### 📦 **Git Version Control**
- **Full Git Workflow:** Each project is a Git repository
- **Auto-Commits:** Every AI change creates a commit
- **LLM-Generated Commit Messages:** Gemini analyzes diffs and writes structured commit messages
- **Commit History:** View all commits with timestamps and diffs
- **Branch Management:** Create, switch, and merge branches
- **Remote Sync:** Fetch, pull, push to remote repositories
- **Time Travel:** Restore to any previous commit

### 💬 **Real-Time Streaming Chat**
- **Server-Sent Events (SSE):** Real-time agent execution streaming
- **Agent Interaction Display:**
  - Thought bubbles (agent reasoning)
  - Tool execution blocks (expandable details)
  - Streaming responses (incremental updates)
- **Event Types:** `start`, `agent_interaction`, `files_ready`, `git_commit`, `reload_preview`, `complete`, `error`
- **Incremental State Saving:** Agent state saved every 3 interactions

### 🖼️ **Multimodal Support**
- **Image Upload:** PNG, JPG, JPEG, GIF, WebP (10MB limit)
- **PDF Upload:** Text extraction and processing
- **AutoGen Integration:** Uses `MultiModalMessage` with `AGImage`
- **Frontend Preview:** Image thumbnails in chat interface

### 💻 **Monaco Editor Integration**
- **Full VSCode Experience:** Powered by Monaco Editor 0.52
- **Syntax Highlighting:** 20+ languages (TypeScript, JavaScript, CSS, HTML, JSON, Python, etc.)
- **Auto-Detection:** Language detected from file extension
- **IntelliSense:** Autocomplete and suggestions
- **Multi-Cursor Support:** Advanced editing capabilities
- **Find/Replace:** Search and replace with regex support

### 🗂️ **Physical File System + Database**
- **Hybrid Architecture:**
  - **Database:** Stores only file metadata (filename, filepath, language, timestamps)
  - **Filesystem:** Stores actual file content at `backend/projects/project_{id}/`
- **Project Scaffolding:** Complete Vite + React + TypeScript template with Tailwind
- **Pre-Installed Dependencies:** lucide-react, date-fns, react-router-dom, zustand, react-query, framer-motion, react-hook-form, zod

---

## 🏆 Comparison: DaveLovable vs. Competitors

| Feature | DaveLovable | Lovable.dev | v0 (Vercel) | Stitch (Google) |
|---------|-------------|-------------|-------------|-----------------|
| **Open Source** | ✅ MIT License | ❌ Proprietary | ❌ Proprietary | ❌ Proprietary |
| **Multi-Agent System** | ✅ 2 agents (Planner + Coder) | ❌ Single agent | ❌ Single agent | ❌ Single agent |
| **Agent Tools** | ✅ 40+ tools (filesystem, git, terminal, web) | ⚠️ Limited | ⚠️ Limited | ⚠️ Limited |
| **Visual Editor** | ✅ Click-to-edit + drag controls | ❌ Text-based only | ❌ Text-based only | ⚠️ Limited |
| **WebContainer Execution** | ✅ Browser-based Node.js | ❌ Server-side preview | ❌ Server-side preview | ⚠️ Unknown |
| **Git Version Control** | ✅ Full git workflow + history | ❌ No git | ❌ No git | ❌ No git |
| **LLM-Generated Commits** | ✅ Auto-generated from diffs | ❌ N/A | ❌ N/A | ❌ N/A |
| **Gemini-3 Flash** | ✅ 1M input tokens | ❌ Claude/GPT-4 | ❌ GPT-4 | ✅ Gemini (likely) |
| **State Persistence** | ✅ Per-project agent memory | ⚠️ Session-based | ⚠️ Session-based | ⚠️ Unknown |
| **Real-Time Streaming** | ✅ SSE with agent interactions | ⚠️ Polling-based | ⚠️ Polling-based | ⚠️ Unknown |
| **Multimodal Input** | ✅ Images + PDFs | ✅ Images | ✅ Images | ⚠️ Unknown |
| **Backend Generation** | ❌ Frontend-only | ✅ Full-stack | ✅ Full-stack | ⚠️ Unknown |
| **Authentication** | ⚠️ In progress | ✅ Full auth | ✅ Full auth | ✅ Full auth |
| **Deployment** | ⚠️ Manual | ✅ Vercel/Netlify | ✅ Vercel | ✅ Google Cloud |

**Legend:** ✅ Full support • ⚠️ Partial/In progress • ❌ Not supported

---

## 🛠️ Technology Stack

### Frontend (`/front`)
- **Core:** React 18.3 + TypeScript 5.8 + Vite 5.4
- **UI:** Tailwind CSS 3.4 + shadcn/ui (Radix UI primitives)
- **State Management:** TanStack Query 5.83
- **Code Editor:** Monaco Editor 0.52 (VSCode-powered)
- **Markdown:** React Markdown with GitHub Flavored Markdown + Syntax Highlighting
- **Icons:** Lucide React 0.462
- **Router:** React Router DOM 6.30
- **WebContainers:** @webcontainer/api 1.6.1

### Backend (`/backend`)
- **Framework:** FastAPI 0.115.5
- **Database:** SQLite with SQLAlchemy 2.0
- **AI Engine:** Microsoft AutoGen 0.7.5 (agentchat + core + OpenAI extension)
- **LLM Provider:** Google Gemini-3 Flash Preview (`gemini-2.0-flash-001`)
- **Security:** JWT (python-jose) + bcrypt (passlib)
- **Screenshot:** Playwright 1.48
- **Image Processing:** Pillow 11.0
- **Utils:** aiohttp, requests, BeautifulSoup4, PyYAML

---

## 🎬 Demo Videos

### 🚀 Full Platform Overview (2-3 minutes)
[![DaveLovable Overview](docs/videos/thumbnails/overview.png)](docs/videos/overview.mp4)

**[Video should show]:**
- Quick intro: "Build React apps with AI in minutes"
- Create new project from landing page
- AI generates initial landing page (show chat → agent execution → preview)
- Quick code edit in Monaco editor
- Switch between different device previews (mobile, tablet, desktop)
- End result: Working app in under 3 minutes

---

### 🤖 Multi-Agent System in Action (1-2 minutes)
[![Multi-Agent Demo](docs/videos/thumbnails/multi-agent.png)](docs/videos/multi-agent.mp4)

**[Video should show]:**
- User request: "Create a dashboard with charts and user table"
- **Planner Agent** breaking down the task into steps (show thought bubble)
- **Coder Agent** executing tools in parallel:
  - `write_file` for Dashboard.tsx (show tool execution block)
  - `write_file` for ChartCard.tsx
  - `write_file` for UserTable.tsx
  - Terminal command: `npm install recharts` (if needed)
- Real-time preview updating with HMR
- Final commit with AI-generated message
- Highlight: ~30 seconds from request to working dashboard

---

### 🎨 Visual Editor Mode (1-2 minutes)
[![Visual Editor Demo](docs/videos/thumbnails/visual-editor.png)](docs/videos/visual-editor.mp4)

**[Video should show]:**
- Existing landing page in preview
- Click button element → shows selection outline (blue border)
- **Style Panel opens** on the right
  - Change background color (show color picker)
  - Change text color
  - Adjust border radius (show drag slider)
  - Modify padding using drag controls (show Shift/Alt modifiers)
- **Element updates in real-time** in preview
- Switch to **Custom Prompt** mode
  - Type: "Make this button have a gradient from purple to pink"
  - Send to agent → agent modifies className
  - Preview updates instantly
- Show final result with gradient button

---

### 📦 Git Version Control & Time Travel (1 minute)
[![Git Demo](docs/videos/thumbnails/git.png)](docs/videos/git.mp4)

**[Video should show]:**
- Project with several AI-generated changes
- Click "Commit History" button (show badge with commit count)
- **Commit History Modal** opens:
  - Show 5-6 commits with AI-generated messages
  - Example: "feat: Add responsive dashboard with chart components"
  - Click commit → show diff viewer (green/red highlights)
- Click "Restore to this commit"
- Preview updates to previous state
- Make new change → new commit created
- Highlight: Full version control with AI-written commit messages

---

### ⚡ WebContainer & Live Preview (1 minute)
[![WebContainer Demo](docs/videos/thumbnails/webcontainer.png)](docs/videos/webcontainer.mp4)

**[Video should show]:**
- Create new project
- **WebContainer loading process:**
  - Show terminal output: "Installing dependencies..."
  - npm install progress
  - Vite dev server starting
  - "Server ready at http://localhost:5173"
- Make code change in Monaco editor (e.g., change text color)
- **Instant HMR update** in preview (no page reload)
- Switch device modes: Desktop → Tablet → Mobile
- Show responsive design working
- **Screenshot capture:** Click button → captures preview → shows thumbnail
- Highlight: True Node.js running in browser, zero backend compute

---

### 🖼️ Multimodal Input (45 seconds)
[![Multimodal Demo](docs/videos/thumbnails/multimodal.png)](docs/videos/multimodal.mp4)

**[Video should show]:**
- User uploads **design mockup image** (PNG)
- Chat message: "Recreate this design"
- Agent analyzes image
- Generates React components matching the design
- Preview shows result side-by-side with mockup
- Upload **PDF** with data table
- Chat: "Create a table component with this data"
- Agent extracts data and creates component
- Highlight: AI understands images and PDFs

---

### 🔄 End-to-End Workflow (3-4 minutes)
[![Full Workflow Demo](docs/videos/thumbnails/workflow.png)](docs/videos/workflow.mp4)

**[Video should show complete user journey]:**
1. **Start:** Landing page → "Create New Project"
2. **Initial Generation:**
   - Request: "Build a task management app"
   - Multi-agent execution (Planner → Coder)
   - First commit: "feat: Initialize task management app"
3. **Iteration 1 - Add Feature:**
   - Request: "Add priority tags to tasks"
   - Agent modifies TaskCard.tsx
   - Preview updates with HMR
   - Commit: "feat: Add priority tag system"
4. **Iteration 2 - Visual Edit:**
   - Click high-priority badge in preview
   - Visual editor: Change color to red
   - Instant update
5. **Iteration 3 - Fix Bug:**
   - Notice completed tasks showing incorrectly
   - Request: "[BUG FIX] Completed tasks should be grayed out"
   - Agent fixes styling
   - Commit: "fix: Gray out completed tasks"
6. **Review History:**
   - Open commit history (4 commits total)
   - Show AI-generated messages
   - Show project evolution
7. **Final Result:**
   - Working task manager with all features
   - Time elapsed: ~4 minutes from idea to app

---

## 📸 Screenshots

### Main Editor Interface
![Editor Interface](docs/screenshots/editor-interface.png)
*Split-panel layout: File explorer, Monaco editor, WebContainer preview, AI chat*

### Visual Editor Mode
![Visual Editor](docs/screenshots/visual-editor.png)
*Click-to-select elements, drag-to-adjust spacing, live style panel*

### Multi-Agent Execution
![Agent Execution](docs/screenshots/agent-execution.png)
*Real-time streaming of agent thoughts, tool calls, and responses*

### Git Version Control
![Git History](docs/screenshots/git-history.png)
*LLM-generated commit messages, commit history, and diff viewer*

---

## 🚀 Quick Start

### Prerequisites
- **Node.js:** 18+ (for frontend)
- **Python:** 3.8+ (for backend)
- **Git:** Latest version
- **Google AI API Key:** Get from [Google AI Studio](https://aistudio.google.com/apikey)

### Installation

#### 1. Clone the repository
```bash
git clone https://github.com/your-username/DaveLovable.git
cd DaveLovable
```

#### 2. Backend Setup
```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env and add your GOOGLE_API_KEY

# Initialize database
python init_db.py

# Install Playwright browsers (for screenshots)
playwright install chromium
```

#### 3. Frontend Setup
```bash
cd ../front

# Install dependencies
npm install
```

#### 4. Run the Application

**Terminal 1 - Backend:**
```bash
cd backend
python run.py
# Backend runs on http://localhost:8000
# API docs: http://localhost:8000/docs
```

**Terminal 2 - Frontend:**
```bash
cd front
npm run dev
# Frontend runs on http://localhost:8080
```

#### 5. Open in Browser
Navigate to [http://localhost:8080](http://localhost:8080) and start building!

---

## 📖 Documentation

### Environment Variables

Create `backend/.env` with the following variables:

```env
# Required: Google AI API Key (get from https://aistudio.google.com/apikey)
GOOGLE_API_KEY=your_google_api_key_here

# Optional: JWT Configuration (not fully implemented)
SECRET_KEY=your_secret_key_here_change_in_production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Optional: Database (defaults to SQLite)
DATABASE_URL=sqlite:///./davelovable.db

# Optional: Debug mode
DEBUG=True

# Optional: AutoGen Configuration
AUTOGEN_MAX_ROUND=20
```

### Development Commands

#### Frontend (`/front`)
```bash
npm run dev          # Start development server (http://localhost:8080)
npm run build        # Build for production
npm run build:dev    # Build in development mode
npm run lint         # Lint code
npm run preview      # Preview production build
```

#### Backend (`/backend`)
```bash
python run.py                          # Start server with run script
uvicorn app.main:app --reload          # Start server with uvicorn
python init_db.py                      # Initialize database
```

### API Endpoints

#### Projects
- `POST /api/v1/projects` - Create project with initial files
- `GET /api/v1/projects` - List all projects for user
- `GET /api/v1/projects/{id}` - Get project with files
- `PUT /api/v1/projects/{id}` - Update project metadata
- `DELETE /api/v1/projects/{id}` - Delete project
- `GET /api/v1/projects/{id}/bundle` - Get all files for WebContainers

#### Files
- `GET /api/v1/projects/{id}/files` - List project files
- `POST /api/v1/projects/{id}/files` - Create new file
- `PUT /api/v1/projects/{id}/files/{file_id}` - Update file content
- `DELETE /api/v1/projects/{id}/files/{file_id}` - Delete file

#### Chat
- `POST /api/v1/chat/{project_id}` - Send message, get AI response with code changes (SSE)
- `GET /api/v1/chat/{project_id}/sessions` - List chat sessions
- `GET /api/v1/chat/{project_id}/sessions/{id}` - Get session with messages

#### Git
- `POST /api/v1/git/{project_id}/commit` - Commit changes
- `GET /api/v1/git/{project_id}/history` - Get commit history
- `GET /api/v1/git/{project_id}/diff` - Get git diff
- `POST /api/v1/git/{project_id}/restore` - Restore to commit

#### Visual Editor
- `POST /api/v1/projects/{id}/visual-edit` - Apply visual edits to components

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                      FRONTEND                           │
│  React + TypeScript + Vite + Tailwind + shadcn/ui      │
│                                                         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐ │
│  │ Monaco Editor│  │ Chat Panel   │  │ Visual Editor│ │
│  │ (Code Edit)  │  │ (AI Chat)    │  │ (Click-Edit) │ │
│  └──────────────┘  └──────────────┘  └──────────────┘ │
│                                                         │
│  ┌─────────────────────────────────────────────────┐  │
│  │   WebContainer Preview (Node.js in Browser)     │  │
│  │   - Vite Dev Server                             │  │
│  │   - HMR (Hot Module Replacement)                │  │
│  │   - Screenshot Capture (html2canvas)            │  │
│  │   - Visual Editor Helper (element selection)    │  │
│  └─────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
                           │ REST API (SSE for chat)
                           ▼
┌─────────────────────────────────────────────────────────┐
│                      BACKEND                            │
│          FastAPI + SQLAlchemy + SQLite                  │
│                                                         │
│  ┌────────────────────────────────────────────────┐   │
│  │  Multi-Agent System (Microsoft AutoGen 0.7)    │   │
│  │                                                 │   │
│  │  ┌─────────────────┐  ┌────────────────────┐  │   │
│  │  │ Planner Agent   │  │    Coder Agent     │  │   │
│  │  │ (Strategy)      │─▶│  (Execution)       │  │   │
│  │  │ No Tools        │  │  40+ Tools         │  │   │
│  │  └─────────────────┘  └────────────────────┘  │   │
│  │           │                    │               │   │
│  │           ▼                    ▼               │   │
│  │  ┌──────────────────────────────────────┐     │   │
│  │  │ SelectorGroupChat (Smart Routing)     │     │   │
│  │  │ - Visual Edit: Direct to Coder        │     │   │
│  │  │ - Bug Fix: Direct to Coder            │     │   │
│  │  │ - Complex: Planner → Coder            │     │   │
│  │  └──────────────────────────────────────┘     │   │
│  └────────────────────────────────────────────────┘   │
│                                                         │
│  ┌────────────────────────────────────────────────┐   │
│  │       Gemini-3 Flash (Google AI)                │   │
│  │  - 1M input tokens, 64K output tokens           │   │
│  │  - Custom thought_signature client              │   │
│  │  - HTTP-level interception for function calls   │   │
│  └────────────────────────────────────────────────┘   │
│                                                         │
│  ┌────────────────────────────────────────────────┐   │
│  │         Physical File System                    │   │
│  │  backend/projects/project_{id}/                 │   │
│  │  ├── .git/           (version control)          │   │
│  │  ├── package.json    (dependencies)             │   │
│  │  ├── vite.config.ts  (build config)             │   │
│  │  ├── src/            (source files)             │   │
│  │  └── .agent_state.json (agent memory)           │   │
│  └────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

### Multi-Agent Workflow

```
User Request
    │
    ▼
┌─────────────────────────────────┐
│   SelectorGroupChat Router       │
│   (Analyzes request context)     │
└─────────────────────────────────┘
    │
    ├─── [VISUAL EDIT] tag? ──────────► Coder Agent (Direct)
    │
    ├─── [BUG FIX] tag? ──────────────► Coder Agent (Direct)
    │
    └─── Complex task? ───────────────► Planner Agent
                                            │
                                            ▼
                                    ┌───────────────────┐
                                    │  Planner thinks   │
                                    │  Creates task list│
                                    └───────────────────┘
                                            │
                                            ▼
                                       Coder Agent
                                            │
                                            ▼
                                    ┌───────────────────┐
                                    │  Executes tools:  │
                                    │  - write_file     │
                                    │  - edit_file      │
                                    │  - run_terminal   │
                                    │  - git commit     │
                                    └───────────────────┘
                                            │
                                            ▼
                                    Files written to disk
                                            │
                                            ▼
                                    Git auto-commit
                                            │
                                            ▼
                                    Frontend syncs to WebContainer
                                            │
                                            ▼
                                    Preview updates (HMR)
```

---

## 🎯 Use Cases

### ✅ Perfect For:
- **Rapid Prototyping:** Build React apps in minutes with AI assistance
- **UI/UX Exploration:** Iterate on designs with visual editor + AI
- **Learning React:** AI explains code and best practices
- **Component Libraries:** Generate reusable components quickly
- **Landing Pages:** Create marketing pages with Tailwind CSS
- **Dashboards:** Build admin panels and data visualizations
- **Portfolio Projects:** Showcase your work with AI-generated code

### ❌ Not Suitable For:
- **Backend Development:** No API/database/server code generation
- **Production Applications:** Authentication and deployment features in progress
- **Large Teams:** No real-time collaboration (single-user only)
- **Enterprise Apps:** No multi-tenancy or advanced security features

---

## 🗺️ Roadmap

### ✅ Completed
- [x] Multi-agent AI orchestration (Planner + Coder)
- [x] 40+ agent tools (filesystem, git, terminal, web)
- [x] WebContainer integration (browser-based Node.js)
- [x] Visual editor mode (click-to-edit + drag controls)
- [x] Git version control with LLM-generated commits
- [x] Real-time streaming chat (SSE)
- [x] Multimodal support (images + PDFs)
- [x] Monaco editor integration
- [x] Project scaffolding (Vite + React + TypeScript + Tailwind)

### 🚧 In Progress
- [ ] User authentication (JWT + bcrypt)
- [ ] Multi-user support
- [ ] Project sharing and collaboration
- [ ] Deployment integration (Vercel/Netlify)
- [ ] Component marketplace

### 🔮 Future
- [ ] Real-time multiplayer editing
- [ ] Custom agent tools (user-defined)
- [ ] Claude 3.5 Sonnet support (alongside Gemini)
- [ ] Mobile app (React Native code generation)
- [ ] Backend code generation (opt-in)
- [ ] AI-powered testing and debugging
- [ ] Performance optimization suggestions
- [ ] Accessibility audits and fixes

---

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

### How to Contribute
1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Commit your changes** (`git commit -m 'Add amazing feature'`)
4. **Push to the branch** (`git push origin feature/amazing-feature`)
5. **Open a Pull Request**

### Development Guidelines
- **Code Style:** Follow existing patterns (TypeScript + Python)
- **Comments:** Write clear, English-only comments
- **Testing:** Add tests for new features (when testing infrastructure is available)
- **Documentation:** Update README and docs for significant changes
- **Commit Messages:** Use conventional commits format

### Areas We Need Help
- [ ] Testing infrastructure (Vitest for frontend, pytest for backend)
- [ ] User authentication implementation
- [ ] Deployment automation
- [ ] Documentation improvements
- [ ] Bug fixes and performance optimizations
- [ ] New agent tools
- [ ] UI/UX enhancements

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Microsoft AutoGen** - For the incredible multi-agent framework
- **Google AI** - For Gemini-3 Flash's blazing-fast performance
- **StackBlitz** - For WebContainers API (browser-based Node.js)
- **Lovable.dev** - For the original inspiration
- **v0 by Vercel** - For pioneering AI-powered UI generation
- **Stitch by Google Labs** - For pushing the boundaries of AI-assisted development
- **shadcn/ui** - For the beautiful component library
- **Monaco Editor** - For the VSCode-powered code editor

---

## 📞 Contact & Support

- **Issues:** [GitHub Issues](https://github.com/your-username/DaveLovable/issues)
- **Discussions:** [GitHub Discussions](https://github.com/your-username/DaveLovable/discussions)
- **Email:** your.email@example.com
- **Twitter:** [@YourTwitterHandle](https://twitter.com/YourTwitterHandle)

---

## ⭐ Star History

If you find this project useful, please give it a star! ⭐

[![Star History Chart](https://api.star-history.com/svg?repos=your-username/DaveLovable&type=Date)](https://star-history.com/#your-username/DaveLovable&Date)

---

<div align="center">

**Built with ❤️ by the DaveLovable Team**

[Website](https://your-website.com) • [Documentation](https://docs.your-website.com) • [Blog](https://blog.your-website.com)

</div>
