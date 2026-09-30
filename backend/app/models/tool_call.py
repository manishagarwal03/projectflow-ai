from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
from app.database import Base


class ToolCall(Base):
    __tablename__ = "tool_calls"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    agent_run_id = Column(UUID(as_uuid=True), ForeignKey("agent_runs.id", ondelete="CASCADE"), nullable=False, index=True)
    tool_type = Column(String(50), nullable=False)  # local_tool | mcp
    tool_name = Column(String(255), nullable=False)
    request_summary = Column(Text, nullable=True)  # NEVER secrets
    response_summary = Column(Text, nullable=True)
    status = Column(String(20), nullable=False)  # success | failed
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    
    # Relationships
    agent_run = relationship("AgentRun", back_populates="tool_calls")
