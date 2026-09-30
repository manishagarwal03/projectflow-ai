from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional, List


class PlanTaskRequest(BaseModel):
    task_context: Optional[str] = None


class AcceptSuggestionsRequest(BaseModel):
    selected_suggestion_ids: List[UUID]


class AgentRunResponse(BaseModel):
    id: UUID
    project_id: Optional[UUID]
    task_id: Optional[UUID]
    agent_type: str
    status: str
    input: str
    output: Optional[str]
    error: Optional[str]
    duration_ms: Optional[int]
    created_at: datetime
    
    class Config:
        from_attributes = True


class AgentRunDetail(AgentRunResponse):
    suggestions: List["AgentSuggestionResponse"] = []
    tool_calls: List["ToolCallResponse"] = []


# Import here to avoid circular dependency
from app.schemas.agent_suggestion import AgentSuggestionResponse
from app.schemas.tool_call import ToolCallResponse

AgentRunDetail.model_rebuild()
