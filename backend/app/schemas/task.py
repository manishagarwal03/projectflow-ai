from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime, date
from typing import Optional, List


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=500)
    description: Optional[str] = None
    priority: str = Field(default="medium", pattern="^(low|medium|high|critical)$")
    status: str = Field(default="todo", pattern="^(todo|in_progress|done)$")
    due_date: Optional[date] = None


class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=500)
    description: Optional[str] = None
    priority: Optional[str] = Field(None, pattern="^(low|medium|high|critical)$")
    status: Optional[str] = Field(None, pattern="^(todo|in_progress|done)$")
    due_date: Optional[date] = None


class TaskResponse(BaseModel):
    id: UUID
    project_id: UUID
    title: str
    description: Optional[str]
    priority: str
    status: str
    due_date: Optional[date]
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class TaskWithRelations(TaskResponse):
    subtasks: List["SubtaskResponse"] = []
    agent_runs: List["AgentRunResponse"] = []


# Import here to avoid circular dependency
from app.schemas.subtask import SubtaskResponse
from app.schemas.agent_run import AgentRunResponse

TaskWithRelations.model_rebuild()
