# ProjectFlow AI

An AI-powered project and task management workspace that helps teams turn goals into actionable plans, coordinate work, surface project context and review progress.

## Features

- **Project & Task Management**: Create, edit, prioritize, filter and track projects and tasks
- **AI-Assisted Planning**: Convert complex tasks into proposed subtasks using the Planning Agent
- **Human-in-the-Loop**: Review and approve AI recommendations before they modify project data
- **Agent Traceability**: Complete history of agent runs, tool calls, and suggestions
- **MCP Integration**: Framework for GitHub integration (stubbed in V1)
- **Dark/Light Mode**: User-switchable theme
- **Responsive Design**: Mobile-first UI that works on phones, tablets, and desktops

## Tech Stack

- **Backend**: Python, FastAPI, SQLAlchemy, Alembic
- **Database**: PostgreSQL
- **Frontend**: Plain HTML, CSS, JavaScript (no framework)
- **Authentication**: JWT tokens with bcrypt password hashing

## Prerequisites

- Python 3.9 or higher
- PostgreSQL 14 or higher
- pip (Python package manager)

## Setup Instructions

### 1. Clone or Navigate to the Project

```bash
cd /Users/manishagarwal/Documents/project-flow
```

### 2. Set Up PostgreSQL Database

#### Install PostgreSQL (macOS)

```bash
# Using Homebrew
brew install postgresql@16

# Start PostgreSQL
brew services start postgresql@16
```

#### Install PostgreSQL (Linux/Ubuntu)

```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
sudo systemctl start postgresql
```

#### Create Database

```bash
# Create database
createdb projectflow_ai

# Or using psql
psql -U postgres
CREATE DATABASE projectflow_ai;
\q
```

### 3. Set Up Python Virtual Environment

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
# venv\Scripts\activate
```

### 4. Install Python Dependencies

```bash
# With virtual environment activated
pip install -r requirements.txt
```

### 5. Configure Environment Variables

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your settings
# On macOS/Linux:
nano .env

# Or use any text editor
```

**Update `.env` with your configuration:**

```env
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/projectflow_ai
SECRET_KEY=your-super-secret-key-here-min-32-characters-long-random-string
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440
CORS_ORIGINS=http://localhost:8000,http://127.0.0.1:8000
```

**Generate a secure SECRET_KEY:**

```bash
python3 -c "import secrets; print(secrets.token_urlsafe(32))"
```

### 6. Run Database Migrations

```bash
# Initialize Alembic (if not already done)
alembic revision --autogenerate -m "Initial migration"

# Run migrations
alembic upgrade head
```

### 7. Start the FastAPI Backend

```bash
# Make sure you're in the backend directory with venv activated
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at: http://localhost:8000

API documentation (Swagger UI): http://localhost:8000/docs

### 8. Start the Frontend

Open a new terminal window:

```bash
# Navigate to frontend directory
cd /Users/manishagarwal/Documents/project-flow/frontend

# Start a simple HTTP server
# Python 3:
python3 -m http.server 8080

# Or Python 2:
# python -m SimpleHTTPServer 8080
```

The frontend will be available at: http://localhost:8080

### 9. Access the Application

1. Open your browser and navigate to: http://localhost:8080
2. Click "Sign Up" to create a new account
3. Fill in your name, email, and password
4. You'll be automatically logged in and redirected to the Projects page

## Usage Guide

### Creating Your First Project

1. Click "+ New Project" button
2. Enter project name, description, and status
3. Click "Create Project"

### Adding Tasks

1. Open a project from the Projects list
2. Click "+ Add Task"
3. Fill in task details (title, description, priority, status, due date)
4. Click "Create Task"

### Using the AI Planning Agent

1. Open a task from the tasks list
2. Click "🤖 Plan with AI"
3. Optionally provide additional context
4. Review the AI-generated subtask suggestions
5. Select the suggestions you want to accept
6. Click "Accept Selected" to create subtasks

### Viewing Agent Activity

1. Navigate to "🤖 Agent Runs" from the sidebar
2. Filter by agent type or status
3. Click "View Details" on any run to see:
   - Input and output
   - Tool calls made by the agent
   - Suggestions generated
   - Execution duration

### Managing Integrations

1. Navigate to "🔗 Integrations" from the sidebar
2. Click "+ Connect GitHub MCP" (stubbed in V1)
3. Enter a configuration reference
4. Test the connection
5. View available tools

### Switching Themes

- Click the "🌙 Dark" or "☀️ Light" button in the sidebar to toggle between dark and light modes
- Your preference is saved in the browser

## Running Tests

```bash
# Navigate to backend directory
cd backend

# Run tests with pytest
pytest

# Run with coverage
pytest --cov=app tests/
```

## Project Structure

```
project-flow/
├── backend/
│   ├── app/
│   │   ├── models/          # SQLAlchemy ORM models
│   │   ├── schemas/         # Pydantic schemas
│   │   ├── routers/         # API endpoints
│   │   ├── services/        # Business logic
│   │   ├── main.py          # FastAPI app
│   │   ├── database.py      # Database config
│   │   ├── config.py        # Settings
│   │   ├── dependencies.py  # Auth dependencies
│   │   └── exceptions.py    # Custom exceptions
│   ├── alembic/             # Database migrations
│   ├── tests/               # Test files
│   ├── requirements.txt
│   ├── .env                 # Environment variables (not committed)
│   └── .env.example
├── frontend/
│   ├── css/
│   │   └── styles.css       # Main stylesheet
│   ├── js/
│   │   ├── api.js           # API client
│   │   ├── auth.js          # Authentication utils
│   │   ├── theme.js         # Dark/light mode
│   │   ├── utils.js         # Utilities
│   │   └── navigation.js    # Navigation utils
│   ├── index.html           # Login/Sign Up
│   ├── projects.html        # Projects list
│   ├── project-form.html    # Create/Edit Project
│   ├── project-detail.html  # Project with tasks
│   ├── task-form.html       # Create/Edit Task
│   ├── task-detail.html     # Task with subtasks
│   ├── ai-plan-review.html  # Review AI suggestions
│   ├── agent-runs.html      # Agent run history
│   ├── agent-run-detail.html # Agent run details
│   └── integrations.html    # MCP integrations
├── AGENTS.md                # Agent instructions
└── README.md                # This file
```

## API Endpoints

### Authentication
- `POST /auth/register` - Create new user account
- `POST /auth/login` - Login with email and password

### Projects
- `GET /projects` - List all projects (with task counts)
- `GET /projects/{id}` - Get project details
- `POST /projects` - Create new project
- `PUT /projects/{id}` - Update project

### Tasks
- `GET /projects/{id}/tasks` - List tasks (with filters)
- `GET /tasks/{id}` - Get task details
- `POST /projects/{id}/tasks` - Create new task
- `PUT /tasks/{id}` - Update task
- `DELETE /tasks/{id}` - Delete task

### AI Planning
- `POST /tasks/{id}/plan` - Invoke Planning Agent

### Agent Runs
- `GET /agent-runs` - List agent runs (with filters)
- `GET /agent-runs/{id}` - Get run details
- `POST /agent-runs/{id}/accept` - Accept suggestions
- `POST /agent-runs/{id}/reject` - Reject plan

### Integrations
- `GET /integrations` - List integrations
- `POST /integrations/github-mcp/connect` - Connect GitHub MCP
- `POST /integrations/{id}/test` - Test integration
- `DELETE /integrations/{id}` - Disconnect integration

## Database Schema

### Tables

1. **users** - User accounts (email, password_hash, status)
2. **projects** - Projects (name, description, status)
3. **tasks** - Tasks (title, description, priority, status, due_date)
4. **subtasks** - Subtasks (title, status, source, agent_run_id)
5. **agent_runs** - AI agent executions
6. **agent_suggestions** - AI-generated suggestions (pending review)
7. **tool_calls** - Sanitized tool/MCP call history
8. **integrations** - External system connections

### Key Relationships

- One User → Many Projects
- One Project → Many Tasks
- One Task → Many Subtasks
- One Task → Many Agent Runs
- One Agent Run → Many Suggestions
- One Agent Run → Many Tool Calls

## Security Features

- ✅ Password hashing with bcrypt (never store plaintext)
- ✅ JWT token authentication
- ✅ User data isolation (users can only access their own data)
- ✅ Environment variables for secrets (never commit .env)
- ✅ CORS protection
- ✅ SQL injection protection (SQLAlchemy ORM)
- ✅ Input validation (Pydantic schemas)

## Troubleshooting

### Backend won't start

- Check that PostgreSQL is running: `pg_isready`
- Verify DATABASE_URL in `.env` is correct
- Ensure virtual environment is activated
- Check for port conflicts on 8000

### Database migration errors

```bash
# Reset database (CAUTION: deletes all data)
alembic downgrade base
alembic upgrade head
```

### Frontend can't connect to backend

- Verify backend is running on http://localhost:8000
- Check CORS_ORIGINS in `.env` includes your frontend origin
- Open browser console (F12) to see error messages

### Authentication issues

- Clear browser localStorage: `localStorage.clear()` in console
- Verify SECRET_KEY is set in `.env`
- Check token expiration (default: 24 hours)

## Future Enhancements (Out of Scope for V1)

- Research Agent for gathering project context
- Reviewer Agent for evaluating work quality
- Team workspaces and role-based permissions
- Real GitHub MCP integration (currently stubbed)
- Document upload (PDF, Word)
- Export reports (Excel, CSV)
- Email notifications
- Background processing for long-running agents
- Advanced dashboards and analytics
- Project dependencies and milestones

## License

Proprietary - All rights reserved

## Support

For issues or questions, contact: Manish Agarwal

---

**Built with ❤️ using FastAPI and PostgreSQL**
