from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID
from app.database import get_db
from app.models.user import User
from app.models.integration import Integration
from app.dependencies import get_current_user
from app.schemas.integration import IntegrationResponse, IntegrationConnect, IntegrationTest
from app.exceptions import NotFoundException, ServiceUnavailableException

router = APIRouter(prefix="/integrations", tags=["Integrations"])


@router.get("", response_model=List[IntegrationResponse])
def list_integrations(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get all configured integrations (stubbed for V1)."""
    integrations = db.query(Integration).all()
    return [IntegrationResponse.model_validate(i) for i in integrations]


@router.post("/github-mcp/connect", status_code=status.HTTP_200_OK)
def connect_github_mcp(
    request: IntegrationConnect,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Configure GitHub MCP integration (stubbed for V1).
    In production, this would validate MCP configuration and establish connection.
    """
    # Check if GitHub MCP integration already exists
    existing = db.query(Integration).filter(
        Integration.provider == "github",
        Integration.integration_type == "mcp"
    ).first()
    
    if existing:
        # Update existing
        existing.status = "connected"
        existing.configuration_reference = request.configuration_reference
        existing.allowed_tools = '["github_list_repos", "github_get_issue", "github_search_code"]'
        db.commit()
        db.refresh(existing)
        integration = existing
    else:
        # Create new
        integration = Integration(
            name="GitHub MCP",
            provider="github",
            integration_type="mcp",
            status="connected",
            configuration_reference=request.configuration_reference,
            allowed_tools='["github_list_repos", "github_get_issue", "github_search_code"]'
        )
        db.add(integration)
        db.commit()
        db.refresh(integration)
    
    return {
        "connection_status": "connected",
        "integration": IntegrationResponse.model_validate(integration)
    }


@router.post("/{integration_id}/test", response_model=IntegrationTest)
def test_integration(
    integration_id: UUID,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Test an integration connection (stubbed for V1).
    In production, this would actually test the MCP connection.
    """
    integration = db.query(Integration).filter(Integration.id == integration_id).first()
    
    if not integration:
        raise NotFoundException(detail="Integration not found")
    
    # Simulate successful test
    if integration.status == "connected":
        return IntegrationTest(
            status="success",
            available_tools=["github_list_repos", "github_get_issue", "github_search_code"]
        )
    else:
        raise ServiceUnavailableException(detail="Integration not connected")


@router.delete("/{integration_id}", status_code=status.HTTP_200_OK)
def disconnect_integration(
    integration_id: UUID,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Disconnect an integration."""
    integration = db.query(Integration).filter(Integration.id == integration_id).first()
    
    if not integration:
        raise NotFoundException(detail="Integration not found")
    
    integration.status = "disconnected"
    db.commit()
    
    return {"disconnected": True}
