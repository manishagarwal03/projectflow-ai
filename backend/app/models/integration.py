from sqlalchemy import Column, String, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid
from app.database import Base


class Integration(Base):
    __tablename__ = "integrations"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    provider = Column(String(100), nullable=False)  # github | future
    integration_type = Column(String(50), nullable=False)  # mcp
    status = Column(String(20), nullable=False, default="disconnected")  # connected | disconnected | error
    configuration_reference = Column(Text, nullable=True)  # Reference only, NEVER raw secret
    allowed_tools = Column(Text, nullable=True)  # JSON array of allowed tool names
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
