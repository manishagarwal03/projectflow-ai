from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session
from typing import List, Optional
from uuid import UUID
from app.database import get_db
from app.models.user import User
from app.models.project import Project
from app.models.task import Task
from app.models.subtask import Subtask
from app.models.agent_run import AgentRun
from app.dependencies import get_current_user
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse, TaskWithRelations
from app.schemas.subtask import SubtaskResponse
from app.schemas.agent_run import AgentRunResponse
from app.exceptions import NotFoundException, UnprocessableEntityException

router = APIRouter(tags=["Tasks"])


@router.get("/projects/{project_id}/tasks", response_model=List[TaskResponse])
def list_tasks(
    project_id: UUID,
    status_filter: Optional[str] = Query(None, alias="status"),
    priority_filter: Optional[str] = Query(None, alias="priority"),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get all tasks for a project with optional filters."""
    # Verify project ownership
    project = db.query(Project).filter(
        Project.id == project_id,
        Project.user_id == current_user.id
    ).first()
    
    if not project:
        raise NotFoundException(detail="Project not found")
    
    # Build query with filters
    query = db.query(Task).filter(Task.project_id == project_id)
    
    if status_filter:
        query = query.filter(Task.status == status_filter)
    if priority_filter:
        query = query.filter(Task.priority == priority_filter)
    
    tasks = query.all()
    return [TaskResponse.model_validate(task) for task in tasks]


@router.get("/tasks/{task_id}", response_model=TaskWithRelations)
def get_task(
    task_id: UUID,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get a specific task with subtasks and agent runs."""
    task = db.query(Task).filter(Task.id == task_id).first()
    
    if not task:
        raise NotFoundException(detail="Task not found")
    
    # Verify ownership through project
    project = db.query(Project).filter(
        Project.id == task.project_id,
        Project.user_id == current_user.id
    ).first()
    
    if not project:
        raise NotFoundException(detail="Task not found")
    
    # Get subtasks
    subtasks = db.query(Subtask).filter(Subtask.task_id == task_id).all()
    
    # Get agent runs
    agent_runs = db.query(AgentRun).filter(AgentRun.task_id == task_id).all()
    
    task_dict = TaskResponse.model_validate(task).model_dump()
    task_dict["subtasks"] = [SubtaskResponse.model_validate(s) for s in subtasks]
    task_dict["agent_runs"] = [AgentRunResponse.model_validate(ar) for ar in agent_runs]
    
    return TaskWithRelations(**task_dict)


@router.post("/projects/{project_id}/tasks", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(
    project_id: UUID,
    task_data: TaskCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Create a new task in a project."""
    # Verify project ownership
    project = db.query(Project).filter(
        Project.id == project_id,
        Project.user_id == current_user.id
    ).first()
    
    if not project:
        raise NotFoundException(detail="Project not found")
    
    # Create new task
    new_task = Task(
        project_id=project_id,
        title=task_data.title,
        description=task_data.description,
        priority=task_data.priority,
        status=task_data.status,
        due_date=task_data.due_date
    )
    
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    
    return TaskResponse.model_validate(new_task)


@router.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: UUID,
    task_data: TaskUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Update a task."""
    task = db.query(Task).filter(Task.id == task_id).first()
    
    if not task:
        raise NotFoundException(detail="Task not found")
    
    # Verify ownership through project
    project = db.query(Project).filter(
        Project.id == task.project_id,
        Project.user_id == current_user.id
    ).first()
    
    if not project:
        raise NotFoundException(detail="Task not found")
    
    # Update fields if provided
    if task_data.title is not None:
        task.title = task_data.title
    if task_data.description is not None:
        task.description = task_data.description
    if task_data.priority is not None:
        task.priority = task_data.priority
    if task_data.status is not None:
        task.status = task_data.status
    if task_data.due_date is not None:
        task.due_date = task_data.due_date
    
    db.commit()
    db.refresh(task)
    
    return TaskResponse.model_validate(task)


@router.delete("/tasks/{task_id}", status_code=status.HTTP_200_OK)
def delete_task(
    task_id: UUID,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Delete a task (and its subtasks via CASCADE)."""
    task = db.query(Task).filter(Task.id == task_id).first()
    
    if not task:
        raise NotFoundException(detail="Task not found")
    
    # Verify ownership through project
    project = db.query(Project).filter(
        Project.id == task.project_id,
        Project.user_id == current_user.id
    ).first()
    
    if not project:
        raise NotFoundException(detail="Task not found")
    
    db.delete(task)
    db.commit()
    
    return {"deleted": True}
