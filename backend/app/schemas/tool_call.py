from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional


class ToolCallResponse(BaseModel):
    id: UUID
    agent_run_id: UUID
    tool_type: str
    tool_name: str
    request_summary: Optional[str]
    response_summary: Optional[str]
    status: str
    created_at: datetime
    
    class Config:
        from_attributes = True
