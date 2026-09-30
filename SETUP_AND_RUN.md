# ProjectFlow AI - Complete Setup and Running Instructions

This document provides complete step-by-step instructions for setting up and running ProjectFlow AI.

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Python Virtual Environment](#python-virtual-environment)
3. [Installing Dependencies](#installing-dependencies)
4. [Configuring PostgreSQL](#configuring-postgresql)
5. [Setting Environment Variables](#setting-environment-variables)
6. [Running Alembic Migrations](#running-alembic-migrations)
7. [Starting FastAPI Backend](#starting-fastapi-backend)
8. [Starting the Frontend](#starting-the-frontend)
9. [Running Tests](#running-tests)
10. [Running the Complete Application](#running-the-complete-application)
11. [Troubleshooting](#troubleshooting)

---

## Prerequisites

Before starting, ensure you have:

- **Python 3.9 or higher**
- **PostgreSQL 14 or higher**
- **pip** (Python package manager)
- **Git** (optional, for version control)

### Check Versions

```bash
python3 --version   # Should be 3.9+
psql --version      # Should be 14+
pip3 --version      # Should be installed
```

---

## 1. Python Virtual Environment

### Creating the Virtual Environment

```bash
# Navigate to the backend directory
cd /Users/manishagarwal/Documents/project-flow/backend

# Create virtual environment
python3 -m venv venv
```

### Activating the Virtual Environment

**On macOS/Linux:**
```bash
source venv/bin/activate
```

**On Windows:**
```bash
venv\Scripts\activate
```

**Verify activation:**
```bash
# Your prompt should now show (venv) prefix
which python  # Should show path to venv/bin/python
```

### Deactivating (When Done)

```bash
deactivate
```

---

## 2. Installing Dependencies

With the virtual environment activated:

```bash
cd /Users/manishagarwal/Documents/project-flow/backend

# Ensure venv is activated
source venv/bin/activate

# Install all dependencies
pip install -r requirements.txt

# Verify installation
pip list
```

**Expected packages:**
- fastapi==0.115.0
- uvicorn[standard]==0.32.0
- sqlalchemy==2.0.36
- alembic==1.14.0
- psycopg2-binary==2.9.10
- pydantic==2.9.2
- python-jose[cryptography]==3.3.0
- passlib[bcrypt]==1.7.4
- pytest==8.3.3
- httpx==0.27.2

---

## 3. Configuring PostgreSQL

### Install PostgreSQL

**On macOS (using Homebrew):**
```bash
brew install postgresql@16
brew services start postgresql@16
```

**On Ubuntu/Debian Linux:**
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

**On Windows:**
- Download installer from postgresql.org
- Run installer and follow instructions
- Start PostgreSQL service from Services panel

### Create Database

**Option A: Using createdb command**
```bash
createdb projectflow_ai
```

**Option B: Using psql**
```bash
# Connect as postgres user
psql -U postgres

# Create database
CREATE DATABASE projectflow_ai;

# Verify creation
\l

# Exit psql
\q
```

### Create PostgreSQL User (Optional)

If you want a dedicated user:

```bash
psql -U postgres

CREATE USER projectflow WITH PASSWORD 'your_secure_password';
GRANT ALL PRIVILEGES ON DATABASE projectflow_ai TO projectflow;

\q
```

### Verify Database Connection

```bash
psql projectflow_ai

# Should connect successfully
# Exit with \q
```

---

## 4. Setting Environment Variables

### Copy Example Environment File

```bash
cd /Users/manishagarwal/Documents/project-flow/backend
cp .env.example .env
```

### Generate Secret Key

```bash
# Generate a secure random secret key
python3 -c "import secrets; print(secrets.token_urlsafe(32))"

# Copy the output (will look like: xJk9s_2Nd8Qp3L...)
```

### Edit .env File

```bash
# Open .env in your preferred editor
nano .env
# or
vim .env
# or
code .env  # VS Code
```

### Configure Environment Variables

**Minimal required configuration:**

```env
# Database connection (update password if needed)
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/projectflow_ai

# JWT secret key (paste the generated key from above)
SECRET_KEY=paste_your_generated_secret_key_here

# JWT algorithm (keep as is)
ALGORITHM=HS256

# Token expiration (24 hours)
ACCESS_TOKEN_EXPIRE_MINUTES=1440

# CORS origins (allow frontend to connect)
CORS_ORIGINS=http://localhost:8000,http://127.0.0.1:8000,http://localhost:8080,http://127.0.0.1:8080
```

### Verify Configuration

```bash
# Test database connection
psql $DATABASE_URL

# Should connect successfully
\q
```

---

## 5. Running Alembic Migrations

Alembic manages database schema migrations.

### Initialize Migration

```bash
cd /Users/manishagarwal/Documents/project-flow/backend

# Ensure venv is activated
source venv/bin/activate

# Generate initial migration
alembic revision --autogenerate -m "Initial schema"

# You should see output like:
# Generating migration file: alembic/versions/abc123_initial_schema.py
```

### Apply Migration

```bash
# Apply all pending migrations
alembic upgrade head

# You should see:
# INFO  [alembic.runtime.migration] Running upgrade -> abc123, Initial schema
```

### Verify Tables Created

```bash
# Connect to database
psql projectflow_ai

# List all tables
\dt

# Expected output:
# public | agent_runs        | table | postgres
# public | agent_suggestions | table | postgres
# public | alembic_version   | table | postgres
# public | integrations      | table | postgres
# public | projects          | table | postgres
# public | subtasks          | table | postgres
# public | tasks             | table | postgres
# public | tool_calls        | table | postgres
# public | users             | table | postgres

# Exit
\q
```

### Common Alembic Commands

```bash
# Check current revision
alembic current

# View migration history
alembic history

# Rollback one migration
alembic downgrade -1

# Rollback all migrations (CAUTION: deletes all data)
alembic downgrade base

# Re-apply all migrations
alembic upgrade head
```

---

## 6. Starting FastAPI Backend

### Start Development Server

```bash
cd /Users/manishagarwal/Documents/project-flow/backend

# Ensure venv is activated
source venv/bin/activate

# Start FastAPI with auto-reload
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Expected output:**
```
INFO:     Will watch for changes in these directories: ['/path/to/backend']
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [12345] using WatchFiles
INFO:     Started server process [12346]
INFO:     Waiting for application startup.
✓ Database connection successful
INFO:     Application startup complete.
```

### Verify Backend is Running

**Option 1: Browser**
- Open http://localhost:8000
- Should see: `{"app":"ProjectFlow AI","version":"1.0.0","status":"running"}`

**Option 2: curl**
```bash
curl http://localhost:8000/

# Expected response:
# {"app":"ProjectFlow AI","version":"1.0.0","status":"running"}
```

**Option 3: API Documentation**
- Open http://localhost:8000/docs
- Should see Swagger UI with all endpoints

### Production Server Options

**For production, use Gunicorn:**

```bash
# Install gunicorn
pip install gunicorn

# Run with multiple workers
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

### Stop Backend

Press `Ctrl+C` in the terminal running uvicorn.

---

## 7. Starting the Frontend

The frontend is pure HTML/CSS/JavaScript and needs a simple HTTP server.

### Start HTTP Server

**Option 1: Python 3 (Recommended)**

```bash
# Open a NEW terminal window (keep backend running)
cd /Users/manishagarwal/Documents/project-flow/frontend

# Start HTTP server on port 8080
python3 -m http.server 8080
```

**Option 2: Python 2**

```bash
cd /Users/manishagarwal/Documents/project-flow/frontend
python -m SimpleHTTPServer 8080
```

**Option 3: Node.js (if installed)**

```bash
cd /Users/manishagarwal/Documents/project-flow/frontend
npx http-server -p 8080
```

**Expected output:**
```
Serving HTTP on 0.0.0.0 port 8080 (http://0.0.0.0:8080/) ...
```

### Verify Frontend is Running

**Open browser:**
- Navigate to http://localhost:8080
- Should see ProjectFlow AI login page

### Production Deployment

For production, use Nginx or Apache:

**Nginx configuration example:**
```nginx
server {
    listen 80;
    server_name your-domain.com;
    
    root /path/to/project-flow/frontend;
    index index.html;
    
    location / {
        try_files $uri $uri/ /index.html;
    }
    
    location /api {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### Stop Frontend

Press `Ctrl+C` in the terminal running the HTTP server.

---

## 8. Running Tests

### Run All Tests

```bash
cd /Users/manishagarwal/Documents/project-flow/backend

# Ensure venv is activated
source venv/bin/activate

# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_auth.py -v
```

### Run Tests with Coverage

```bash
# Install coverage (if not already installed)
pip install pytest-cov

# Run with coverage report
pytest --cov=app tests/

# Generate HTML coverage report
pytest --cov=app --cov-report=html tests/

# Open coverage report
open htmlcov/index.html  # macOS
# or
xdg-open htmlcov/index.html  # Linux
```

### Expected Test Output

```
================================ test session starts =================================
platform darwin -- Python 3.11.5, pytest-8.3.3, pluggy-1.5.0
collected 4 items

tests/test_auth.py ....                                                        [100%]

================================= 4 passed in 1.23s ==================================
```

---

## 9. Running the Complete Application

### Full Startup Sequence

**Terminal 1: Backend**
```bash
cd /Users/manishagarwal/Documents/project-flow/backend
source venv/bin/activate
uvicorn app.main:app --reload
```

**Terminal 2: Frontend**
```bash
cd /Users/manishagarwal/Documents/project-flow/frontend
python3 -m http.server 8080
```

**Terminal 3: Database (Optional)**
```bash
# Keep a psql session open for monitoring
psql projectflow_ai
```

### First-Time User Journey

1. **Open Browser** → http://localhost:8080

2. **Sign Up**
   - Click "Sign Up"
   - Enter name: "Test User"
   - Enter email: "test@example.com"
   - Enter password: "password123"
   - Click "Sign Up"
   - Should redirect to Projects page

3. **Create Project**
   - Click "+ New Project"
   - Name: "My First Project"
   - Description: "Testing ProjectFlow AI"
   - Status: "Active"
   - Click "Create Project"
   - Should redirect to Project Detail page

4. **Add Task**
   - Click "+ Add Task"
   - Title: "Implement user authentication"
   - Description: "Add JWT auth to the API"
   - Priority: "High"
   - Status: "To Do"
   - Click "Create Task"
   - Should redirect to Task Detail page

5. **Use AI Planning**
   - Click "🤖 Plan with AI"
   - Enter context (optional): "Use bcrypt for password hashing"
   - Wait for agent to complete
   - Should redirect to AI Plan Review page

6. **Review Suggestions**
   - Check boxes next to suggestions you want
   - Click "Accept Selected"
   - Should redirect back to Task Detail
   - Verify subtasks are now visible

7. **View Agent History**
   - Click "🤖 Agent Runs" in sidebar
   - Should see your planning run
   - Click "View Details"
   - Should see input, output, and tool calls

8. **Toggle Dark Mode**
   - Click "🌙 Dark" button in sidebar
   - UI should switch to dark theme
   - Reload page - theme should persist

### Verify Everything Works

**Backend Health:**
```bash
curl http://localhost:8000/
# Expected: {"app":"ProjectFlow AI",...}
```

**Frontend Access:**
```bash
curl http://localhost:8080/
# Expected: HTML content of index.html
```

**Database Connection:**
```bash
psql projectflow_ai -c "SELECT COUNT(*) FROM users;"
# Expected: count row
```

**API Authentication:**
```bash
# Register user
curl -X POST http://localhost:8000/auth/register \
  -H "Content-Type: application/json" \
  -d '{"name":"API Test","email":"api@test.com","password":"test123"}'

# Expected: {"access_token":"...","token_type":"bearer","user":{...}}
```

---

## 10. Troubleshooting

### Backend Won't Start

**Error: `ModuleNotFoundError: No module named 'app'`**

**Solution:**
```bash
# Verify you're in backend directory
pwd
# Should be: /Users/manishagarwal/Documents/project-flow/backend

# Verify venv is activated
which python
# Should show venv/bin/python

# Reinstall dependencies
pip install -r requirements.txt
```

**Error: `psycopg2.OperationalError: could not connect to server`**

**Solution:**
```bash
# Check if PostgreSQL is running
pg_isready

# If not running, start it:
# macOS:
brew services start postgresql@16

# Linux:
sudo systemctl start postgresql

# Windows: Start PostgreSQL service from Services
```

**Error: `SECRET_KEY environment variable is not set`**

**Solution:**
```bash
# Verify .env file exists
ls -la .env

# If missing, copy example
cp .env.example .env

# Edit and add SECRET_KEY
nano .env
```

### Frontend Won't Load

**Error: `Failed to load projects: NetworkError`**

**Solution:**
1. Verify backend is running: http://localhost:8000
2. Check CORS configuration in `.env`:
   ```env
   CORS_ORIGINS=http://localhost:8080
   ```
3. Restart backend after changing `.env`

**Error: `401 Unauthorized`**

**Solution:**
```javascript
// Open browser console (F12) and run:
localStorage.clear();
// Then reload page and login again
```

### Database Migration Errors

**Error: `sqlalchemy.exc.ProgrammingError: relation does not exist`**

**Solution:**
```bash
# Check migration status
alembic current

# If no migrations applied:
alembic upgrade head

# If migrations exist but tables missing:
alembic downgrade base
alembic upgrade head
```

**Error: `Target database is not up to date`**

**Solution:**
```bash
# Generate new migration
alembic revision --autogenerate -m "Update schema"

# Apply migration
alembic upgrade head
```

### Port Already in Use

**Error: `Address already in use`**

**Solution:**
```bash
# Find process using port 8000
lsof -i :8000

# Kill process
kill -9 <PID>

# Or use different port
uvicorn app.main:app --port 8001
```

### Permission Denied

**Error: `PermissionError: [Errno 13] Permission denied`**

**Solution:**
```bash
# Check file permissions
ls -la

# Fix permissions
chmod +x venv/bin/activate

# Or use sudo (not recommended for venv)
```

---

## Quick Reference Commands

### Daily Development Workflow

```bash
# Terminal 1: Backend
cd ~/Documents/project-flow/backend
source venv/bin/activate
uvicorn app.main:app --reload

# Terminal 2: Frontend
cd ~/Documents/project-flow/frontend
python3 -m http.server 8080

# Terminal 3: Database monitoring
psql projectflow_ai

# In psql:
\dt                    # List tables
SELECT * FROM users;   # Query users
\q                     # Exit
```

### Shutdown Sequence

```bash
# 1. Stop frontend (Terminal 2)
Ctrl+C

# 2. Stop backend (Terminal 1)
Ctrl+C

# 3. Deactivate venv
deactivate

# 4. Stop PostgreSQL (optional)
brew services stop postgresql@16  # macOS
sudo systemctl stop postgresql    # Linux
```

### Reset Everything

```bash
# CAUTION: This deletes all data

# 1. Drop database
dropdb projectflow_ai

# 2. Recreate database
createdb projectflow_ai

# 3. Run migrations
cd backend
source venv/bin/activate
alembic upgrade head

# 4. Clear browser storage
# Open browser console: localStorage.clear()
```

---

## Environment URLs

- **Backend API**: http://localhost:8000
- **API Docs (Swagger)**: http://localhost:8000/docs
- **API Docs (ReDoc)**: http://localhost:8000/redoc
- **Frontend**: http://localhost:8080
- **PostgreSQL**: localhost:5432

---

## Support

For issues:
1. Check [TROUBLESHOOTING](#troubleshooting) section above
2. Review logs in terminal
3. Check browser console (F12) for frontend errors
4. Verify all services are running
5. Consult README.md for additional documentation

---

**🎉 You're ready to use ProjectFlow AI!**
