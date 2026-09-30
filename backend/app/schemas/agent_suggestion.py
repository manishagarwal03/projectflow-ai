from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional


class AgentSuggestionResponse(BaseModel):
    id: UUID
    agent_run_id: UUID
    suggestion_type: str
    title: str
    description: Optional[str]
    status: str
    created_at: datetime
    
    class Config:
        from_attributes = True
