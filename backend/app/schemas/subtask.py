from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional


class SubtaskResponse(BaseModel):
    id: UUID
    task_id: UUID
    title: str
    status: str
    source: str
    agent_run_id: Optional[UUID]
    created_at: datetime
    
    class Config:
        from_attributes = True
