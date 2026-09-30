from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List
from uuid import UUID
from app.database import get_db
from app.models.user import User
from app.models.project import Project
from app.models.task import Task
from app.dependencies import get_current_user
from app.schemas.project import ProjectCreate, ProjectUpdate, ProjectResponse, ProjectWithCounts
from app.exceptions import NotFoundException

router = APIRouter(prefix="/projects", tags=["Projects"])


@router.get("", response_model=List[ProjectWithCounts])
def list_projects(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get all projects for the current user with task counts."""
    projects = db.query(Project).filter(Project.user_id == current_user.id).all()
    
    result = []
    for project in projects:
        # Calculate task counts
        tasks = db.query(Task).filter(Task.project_id == project.id).all()
        total_tasks = len(tasks)
        todo_tasks = sum(1 for t in tasks if t.status == "todo")
        in_progress_tasks = sum(1 for t in tasks if t.status == "in_progress")
        done_tasks = sum(1 for t in tasks if t.status == "done")
        completion_percentage = (done_tasks / total_tasks * 100) if total_tasks > 0 else 0.0
        
        project_dict = ProjectResponse.model_validate(project).model_dump()
        project_dict.update({
            "total_tasks": total_tasks,
            "todo_tasks": todo_tasks,
            "in_progress_tasks": in_progress_tasks,
            "done_tasks": done_tasks,
            "completion_percentage": round(completion_percentage, 2)
        })
        result.append(ProjectWithCounts(**project_dict))
    
    return result


@router.get("/{project_id}", response_model=ProjectWithCounts)
def get_project(
    project_id: UUID,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get a specific project with task counts."""
    project = db.query(Project).filter(
        Project.id == project_id,
        Project.user_id == current_user.id
    ).first()
    
    if not project:
        raise NotFoundException(detail="Project not found")
    
    # Calculate task counts
    tasks = db.query(Task).filter(Task.project_id == project.id).all()
    total_tasks = len(tasks)
    todo_tasks = sum(1 for t in tasks if t.status == "todo")
    in_progress_tasks = sum(1 for t in tasks if t.status == "in_progress")
    done_tasks = sum(1 for t in tasks if t.status == "done")
    completion_percentage = (done_tasks / total_tasks * 100) if total_tasks > 0 else 0.0
    
    project_dict = ProjectResponse.model_validate(project).model_dump()
    project_dict.update({
        "total_tasks": total_tasks,
        "todo_tasks": todo_tasks,
        "in_progress_tasks": in_progress_tasks,
        "done_tasks": done_tasks,
        "completion_percentage": round(completion_percentage, 2)
    })
    
    return ProjectWithCounts(**project_dict)


@router.post("", response_model=ProjectResponse, status_code=status.HTTP_201_CREATED)
def create_project(
    project_data: ProjectCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Create a new project."""
    new_project = Project(
        user_id=current_user.id,
        name=project_data.name,
        description=project_data.description,
        status=project_data.status
    )
    
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    
    return ProjectResponse.model_validate(new_project)


@router.put("/{project_id}", response_model=ProjectResponse)
def update_project(
    project_id: UUID,
    project_data: ProjectUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Update a project."""
    project = db.query(Project).filter(
        Project.id == project_id,
        Project.user_id == current_user.id
    ).first()
    
    if not project:
        raise NotFoundException(detail="Project not found")
    
    # Update fields if provided
    if project_data.name is not None:
        project.name = project_data.name
    if project_data.description is not None:
        project.description = project_data.description
    if project_data.status is not None:
        project.status = project_data.status
    
    db.commit()
    db.refresh(project)
    
    return ProjectResponse.model_validate(project)
