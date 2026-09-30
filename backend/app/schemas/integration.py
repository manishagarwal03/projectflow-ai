from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional, List


class IntegrationConnect(BaseModel):
    configuration_reference: str


class IntegrationTest(BaseModel):
    status: str
    available_tools: List[str] = []


class IntegrationResponse(BaseModel):
    id: UUID
    name: str
    provider: str
    integration_type: str
    status: str
    configuration_reference: Optional[str]
    allowed_tools: Optional[str]
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True
