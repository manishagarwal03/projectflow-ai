# ProjectFlow AI - Agent Instructions

## Source of Truth

The project blueprint JSON is the source of truth for product
requirements, screens, APIs, database schema, business rules and scope.

Read the relevant blueprint requirements before implementing changes.

Do not invent product requirements that are not in the blueprint.

If a product, business-rule, data-model, security or architectural
decision is required but is not covered by the blueprint, ask before
proceeding.

For routine implementation decisions that do not change product
behavior or architecture, use standard engineering practices.

Blueprint sections map to code as follows:

- **derived.api_endpoints** → Backend routers (app/routers/)
- **answers.database_tables_and_fields** → Database models (app/models/)
- **answers.front_end_screens_and_controls** → Frontend pages (frontend/*.html)
- **answers.back_end_business_rules_and_calculations** → Business logic validation
- **answers.back_end_error_situations_and_messages** → Exception handling
- **answers.front_end_most_important_user_journey_step_by_step** → Integration tests and user flows

When the blueprint specifies exact field names, enum values, status codes, or error messages, use them verbatim. For example:
- Task status must be "todo", "in_progress", or "done" (not "pending", "completed")
- Project status must be "active", "paused", or "completed"
- Subtask source must be "manual" or "ai"

Check the blueprint's derived.api_endpoints for the exact request/response contract before implementing or modifying endpoints.

## Technology

Use:

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Plain HTML, CSS and JavaScript

Keep API, business logic, database access and frontend concerns
separated.

## Code Organization

The backend follows a layered FastAPI architecture:

- **app/models/** - SQLAlchemy database models (one file per table)
- **app/schemas/** - Pydantic validation schemas for requests/responses
- **app/routers/** - API endpoint definitions (route handlers only)
- **app/services/** - Business logic and external integrations
- **app/dependencies.py** - Reusable dependencies like authentication
- **app/exceptions.py** - Custom exception classes
- **app/database.py** - Database connection and session management
- **app/config.py** - Environment configuration

When implementing new features:
1. Create/update models first (database layer)
2. Define schemas for validation (API contract)
3. Implement business logic in services if complex
4. Add routers last (wire everything together)

Frontend structure:
- **frontend/*.html** - Each screen is a separate page
- **frontend/js/api.js** - Centralized API client (add all endpoints here)
- **frontend/js/auth.js** - Authentication utilities
- **frontend/js/utils.js** - Shared helper functions
- **frontend/css/styles.css** - Single stylesheet for all pages

## Database Conventions

All tables follow these patterns:

1. **Primary Keys**: Always use UUID, never integers
   ```python
   id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
   ```

2. **Foreign Keys**: Always include CASCADE for parent-child relationships
   ```python
   project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id", ondelete="CASCADE"), nullable=False, index=True)
   ```

3. **Timestamps**: Every table includes created_at and updated_at
   ```python
   created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
   updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
   ```

4. **Unique Constraints**: Define in model for business rules (e.g., email uniqueness)
   ```python
   email = Column(String(255), unique=True, nullable=False, index=True)
   ```

5. **Relationships**: Define bidirectional relationships with back_populates
   ```python
   # In Project model
   tasks = relationship("Task", back_populates="project", cascade="all, delete-orphan")
   # In Task model
   project = relationship("Project", back_populates="tasks")
   ```

After creating or modifying models, always generate and run migrations:
```bash
alembic revision --autogenerate -m "Description"
alembic upgrade head
```

## API Patterns

All protected endpoints follow this structure:

1. **Authentication**: Use dependency injection
   ```python
   def endpoint(
       current_user: User = Depends(get_current_user),
       db: Session = Depends(get_db)
   ):
   ```

2. **Ownership Verification**: Always verify the user owns the resource
   ```python
   project = db.query(Project).filter(
       Project.id == project_id,
       Project.user_id == current_user.id
   ).first()
   
   if not project:
       raise NotFoundException(detail="Project not found")
   ```

3. **Exception Handling**: Use custom exception classes from app/exceptions.py
   - `NotFoundException` - 404 errors
   - `ConflictException` - 409 conflicts (e.g., duplicate email)
   - `UnprocessableEntityException` - 422 validation errors
   - `ServiceUnavailableException` - 503 service errors

4. **Response Models**: Always specify response_model in decorator
   ```python
   @router.get("/projects/{project_id}", response_model=ProjectWithCounts)
   ```

5. **Frontend API Calls**: All endpoints must be added to frontend/js/api.js
   - Keeps API client centralized
   - Automatic auth header injection
   - Consistent error handling

Never expose internal errors, user IDs of other users, or implementation details in API responses.

## Frontend Patterns

The frontend uses plain HTML pages with shared JavaScript modules:

1. **Page Structure**: Every authenticated page includes
   - Sidebar with navigation and theme toggle
   - Main content area with header
   - Shared scripts loaded in this order:
     ```html
     <script src="js/theme.js"></script>
     <script src="js/api.js"></script>
     <script src="js/auth.js"></script>
     <script src="js/utils.js"></script>
     <script src="js/navigation.js"></script>
     ```

2. **Authentication**: Every protected page starts with
   ```javascript
   requireAuth(); // Redirects to login if no token
   ```

3. **Navigation**: Use query parameters for IDs
   - `project-detail.html?id={project_id}`
   - `task-detail.html?id={task_id}`
   - Extract with: `new URLSearchParams(window.location.search).get('id')`

4. **Theming**: All colors use CSS variables
   - Theme toggle: `toggleTheme()` from theme.js
   - Colors: `--bg-primary`, `--text-primary`, `--color-primary`, etc.
   - Never hardcode colors in HTML or inline styles

5. **Error Handling**: Use `showAlert()` from utils.js for user feedback

6. **API Integration**: Always use the `api` client from api.js
   ```javascript
   const projects = await api.getProjects();
   ```

When adding new pages, copy the structure from an existing page to maintain consistency.

## Design

Follow the design requirements defined in the blueprint.

Keep the UI:

- Clean and professional
- Simple to navigate
- Consistent across screens
- Responsive
- Clear about task status, priority and primary actions

Do not introduce a different design system without approval.

## Security

- Never hard-code or commit secrets.
- Never store plaintext passwords.
- Enforce authentication on the backend.
- Enforce user ownership and authorization on the backend.
- Never allow users to access another user's data.
- Never expose internal errors, credentials or secrets to the frontend.

## Working Style

- Inspect existing code before changing it.
- Plan substantial changes before implementing them.
- Make small, focused changes.
- Do not modify unrelated functionality.
- Do not add features that were not requested.
- Preserve existing behavior unless the requirement changes it.
- Prefer extending existing code over unnecessarily rewriting it.

## Verification

After making a change:

1. Run relevant tests.
   - Backend tests: `cd backend && pytest tests/` (requires test database)
   - Test specific module: `pytest tests/test_auth.py`
   - When modifying authentication: Run test_auth.py
   - When modifying API endpoints: Test with both valid and invalid auth
   - When changing database models: Verify migrations work
   - Manual frontend testing required (no automated tests in V1)
   
   If changes affect authentication, ownership, or security rules, test with:
   - Unauthenticated requests (should return 401)
   - Different user accounts (should not access each other's data)
   - Invalid tokens (should return 401)

2. Fix failures introduced by the change.
3. Review the final changes.
4. Report what changed.
5. Report what was actually tested.
6. Report anything that could not be verified.

Never claim something works unless it was actually verified.

## Improving These Instructions

While working, identify recurring problems, useful conventions or
repository-specific practices that could improve future work.

Do not modify AGENTS.md automatically.

When you identify a useful improvement:

1. Explain the problem or recurring pattern.
2. Propose the exact change to AGENTS.md.
3. Explain why the rule would be useful for future tasks.
4. Ask for approval.
5. Update AGENTS.md only after approval.

Do not add one-off implementation details to AGENTS.md.

Only propose instructions that are likely to remain useful across
multiple future tasks.

Before proposing a new instruction, check whether an existing
instruction already covers it.