# ProjectFlow AI - Quick Start Guide

This guide will get you up and running in 5 minutes.

## Prerequisites Check

```bash
# Check Python version (need 3.9+)
python3 --version

# Check PostgreSQL (need 14+)
psql --version

# If not installed, follow README.md setup instructions
```

## Quick Setup

### 1. Create and Activate Virtual Environment

```bash
cd /Users/manishagarwal/Documents/project-flow/backend
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
# venv\Scripts\activate  # On Windows
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Create PostgreSQL Database

```bash
# Option A: Using createdb command
createdb projectflow_ai

# Option B: Using psql
psql -U postgres -c "CREATE DATABASE projectflow_ai;"
```

### 4. Configure Environment

```bash
# Copy example env file
cp .env.example .env

# Generate a secret key
python3 -c "import secrets; print(secrets.token_urlsafe(32))"

# Edit .env and paste the secret key
nano .env
```

**Minimal `.env` configuration:**

```env
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/projectflow_ai
SECRET_KEY=<paste-generated-secret-key-here>
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440
CORS_ORIGINS=http://localhost:8000,http://127.0.0.1:8000,http://localhost:8080,http://127.0.0.1:8080
```

### 5. Run Database Migrations

```bash
# Generate initial migration
alembic revision --autogenerate -m "Initial schema"

# Apply migrations
alembic upgrade head
```

### 6. Start the Backend

```bash
# Make sure virtual environment is activated
uvicorn app.main:app --reload
```

✅ Backend running at: http://localhost:8000

### 7. Start the Frontend (New Terminal)

```bash
cd /Users/manishagarwal/Documents/project-flow/frontend
python3 -m http.server 8080
```

✅ Frontend running at: http://localhost:8080

## First Steps

1. **Open your browser** → http://localhost:8080
2. **Sign Up** with your name, email, and password
3. **Create a Project** → Click "+ New Project"
4. **Add a Task** → Open the project, click "+ Add Task"
5. **Try AI Planning** → Open the task, click "🤖 Plan with AI"
6. **Review Suggestions** → Select suggestions and click "Accept Selected"

## Verify Everything Works

### Test Backend API

```bash
# In a new terminal
curl http://localhost:8000/

# Expected response:
# {"app":"ProjectFlow AI","version":"1.0.0","status":"running"}
```

### Test Database Connection

```bash
# Connect to database
psql projectflow_ai

# List tables
\dt

# Expected tables:
# users, projects, tasks, subtasks, agent_runs, 
# agent_suggestions, tool_calls, integrations, alembic_version

# Exit psql
\q
```

### Run Tests

```bash
cd /Users/manishagarwal/Documents/project-flow/backend
pytest tests/test_auth.py -v
```

## Common Issues & Fixes

### "ModuleNotFoundError: No module named 'app'"

**Fix:** Make sure you're in the `backend` directory and virtual environment is activated:

```bash
cd backend
source venv/bin/activate
```

### "psycopg2.OperationalError: could not connect to server"

**Fix:** Start PostgreSQL:

```bash
# macOS
brew services start postgresql@16

# Linux
sudo systemctl start postgresql
```

### "sqlalchemy.exc.ProgrammingError: relation does not exist"

**Fix:** Run database migrations:

```bash
cd backend
alembic upgrade head
```

### Frontend shows "Failed to load" errors

**Fix:** Verify backend is running and CORS is configured:

1. Check backend is running: http://localhost:8000
2. Check CORS_ORIGINS in `.env` includes `http://localhost:8080`
3. Restart backend after changing `.env`

### "401 Unauthorized" errors

**Fix:** Clear browser storage and re-login:

```javascript
// Open browser console (F12) and run:
localStorage.clear();
// Then reload page and login again
```

## Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Review [AGENTS.md](AGENTS.md) for development guidelines
- Explore the API documentation: http://localhost:8000/docs

## Stopping the Application

```bash
# Stop backend: Press Ctrl+C in the backend terminal
# Stop frontend: Press Ctrl+C in the frontend terminal

# Deactivate virtual environment
deactivate

# Stop PostgreSQL (optional)
brew services stop postgresql@16  # macOS
sudo systemctl stop postgresql    # Linux
```

## Development Workflow

```bash
# Terminal 1: Backend
cd backend
source venv/bin/activate
uvicorn app.main:app --reload

# Terminal 2: Frontend
cd frontend
python3 -m http.server 8080

# Terminal 3: Database operations
psql projectflow_ai
```

---

**🎉 You're all set! Happy coding!**
