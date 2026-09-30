from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session
from typing import List, Optional
from uuid import UUID
from app.database import get_db
from app.models.user import User
from app.models.project import Project
from app.models.task import Task
from app.models.agent_run import AgentRun
from app.models.agent_suggestion import AgentSuggestion
from app.models.subtask import Subtask
from app.models.tool_call import ToolCall
from app.dependencies import get_current_user
from app.schemas.agent_run import (
    AgentRunResponse,
    AgentRunDetail,
    PlanTaskRequest,
    AcceptSuggestionsRequest
)
from app.schemas.agent_suggestion import AgentSuggestionResponse
from app.schemas.tool_call import ToolCallResponse
from app.schemas.subtask import SubtaskResponse
from app.services.planning_agent import plan_task
from app.exceptions import NotFoundException, ServiceUnavailableException

router = APIRouter(tags=["Agent Runs"])


@router.post("/tasks/{task_id}/plan", status_code=status.HTTP_200_OK)
def create_task_plan(
    task_id: UUID,
    request: PlanTaskRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Invoke Planning Agent to generate subtask suggestions."""
    # Get task and verify ownership
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise NotFoundException(detail="Task not found")
    
    project = db.query(Project).filter(
        Project.id == task.project_id,
        Project.user_id == current_user.id
    ).first()
    if not project:
        raise NotFoundException(detail="Task not found")
    
    try:
        # Invoke planning agent
        agent_run = plan_task(task, request.task_context or "", db)
        
        # Get suggestions
        suggestions = db.query(AgentSuggestion).filter(
            AgentSuggestion.agent_run_id == agent_run.id
        ).all()
        
        return {
            "agent_run_id": agent_run.id,
            "suggested_subtasks": [
                AgentSuggestionResponse.model_validate(s) for s in suggestions
            ]
        }
    except Exception as e:
        raise ServiceUnavailableException(detail="Planning agent encountered an error")


@router.get("/agent-runs", response_model=List[AgentRunResponse])
def list_agent_runs(
    agent_type: Optional[str] = Query(None),
    status_filter: Optional[str] = Query(None, alias="status"),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get all agent runs for the current user with optional filters."""
    # Get all projects for user
    project_ids = [p.id for p in db.query(Project.id).filter(
        Project.user_id == current_user.id
    ).all()]
    
    # Build query
    query = db.query(AgentRun).filter(AgentRun.project_id.in_(project_ids))
    
    if agent_type:
        query = query.filter(AgentRun.agent_type == agent_type)
    if status_filter:
        query = query.filter(AgentRun.status == status_filter)
    
    agent_runs = query.order_by(AgentRun.created_at.desc()).all()
    return [AgentRunResponse.model_validate(ar) for ar in agent_runs]


@router.get("/agent-runs/{agent_run_id}", response_model=AgentRunDetail)
def get_agent_run(
    agent_run_id: UUID,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get detailed information about a specific agent run."""
    agent_run = db.query(AgentRun).filter(AgentRun.id == agent_run_id).first()
    
    if not agent_run:
        raise NotFoundException(detail="Agent run not found")
    
    # Verify ownership through project
    if agent_run.project_id:
        project = db.query(Project).filter(
            Project.id == agent_run.project_id,
            Project.user_id == current_user.id
        ).first()
        if not project:
            raise NotFoundException(detail="Agent run not found")
    
    # Get suggestions
    suggestions = db.query(AgentSuggestion).filter(
        AgentSuggestion.agent_run_id == agent_run_id
    ).all()
    
    # Get tool calls
    tool_calls = db.query(ToolCall).filter(
        ToolCall.agent_run_id == agent_run_id
    ).all()
    
    run_dict = AgentRunResponse.model_validate(agent_run).model_dump()
    run_dict["suggestions"] = [AgentSuggestionResponse.model_validate(s) for s in suggestions]
    run_dict["tool_calls"] = [ToolCallResponse.model_validate(tc) for tc in tool_calls]
    
    return AgentRunDetail(**run_dict)


@router.post("/agent-runs/{agent_run_id}/accept", status_code=status.HTTP_200_OK)
def accept_suggestions(
    agent_run_id: UUID,
    request: AcceptSuggestionsRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Accept selected suggestions and create subtasks."""
    agent_run = db.query(AgentRun).filter(AgentRun.id == agent_run_id).first()
    
    if not agent_run:
        raise NotFoundException(detail="Agent run not found")
    
    # Verify ownership
    if agent_run.project_id:
        project = db.query(Project).filter(
            Project.id == agent_run.project_id,
            Project.user_id == current_user.id
        ).first()
        if not project:
            raise NotFoundException(detail="Agent run not found")
    
    # Get and validate suggestions
    suggestions = db.query(AgentSuggestion).filter(
        AgentSuggestion.id.in_(request.selected_suggestion_ids),
        AgentSuggestion.agent_run_id == agent_run_id,
        AgentSuggestion.status == "pending"
    ).all()
    
    if not suggestions:
        raise NotFoundException(detail="No valid suggestions found")
    
    # Create subtasks from accepted suggestions
    created_subtasks = []
    for suggestion in suggestions:
        if suggestion.suggestion_type == "subtask":
            subtask = Subtask(
                task_id=agent_run.task_id,
                title=suggestion.title,
                status="todo",
                source="ai",
                agent_run_id=agent_run.id
            )
            db.add(subtask)
            created_subtasks.append(subtask)
            
            # Mark suggestion as accepted
            suggestion.status = "accepted"
    
    db.commit()
    
    # Refresh to get IDs
    for subtask in created_subtasks:
        db.refresh(subtask)
    
    return {
        "created_subtasks": [SubtaskResponse.model_validate(s) for s in created_subtasks]
    }


@router.post("/agent-runs/{agent_run_id}/reject", status_code=status.HTTP_200_OK)
def reject_plan(
    agent_run_id: UUID,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Reject an agent run and its suggestions."""
    agent_run = db.query(AgentRun).filter(AgentRun.id == agent_run_id).first()
    
    if not agent_run:
        raise NotFoundException(detail="Agent run not found")
    
    # Verify ownership
    if agent_run.project_id:
        project = db.query(Project).filter(
            Project.id == agent_run.project_id,
            Project.user_id == current_user.id
        ).first()
        if not project:
            raise NotFoundException(detail="Agent run not found")
    
    # Mark agent run as rejected
    agent_run.status = "rejected"
    
    # Mark all pending suggestions as rejected
    suggestions = db.query(AgentSuggestion).filter(
        AgentSuggestion.agent_run_id == agent_run_id,
        AgentSuggestion.status == "pending"
    ).all()
    
    for suggestion in suggestions:
        suggestion.status = "rejected"
    
    db.commit()
    
    return {"status": "rejected"}
