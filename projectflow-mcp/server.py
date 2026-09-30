import os
import httpx

from dotenv import load_dotenv
from mcp.server import MCPServer

load_dotenv()
mcp = MCPServer("ProjectFlow")

def get_config():
    token = os.environ["PROJECTFLOW_ACCESS_TOKEN"]
    api_url = os.environ.get(
        "PROJECTFLOW_API_URL",
        "http://localhost:8000"
    )

    headers = {
        "Authorization": f"Bearer {token}"
    }

    return api_url, headers


@mcp.tool()
async def list_projects() -> dict:
    """List projects belonging to the authenticated ProjectFlow user."""

    api_url, headers = get_config()

    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{api_url}/projects",
            headers=headers
        )

        response.raise_for_status()
        return response.json()


@mcp.tool()
async def get_project(project_id: str) -> dict:
    """Get details of a specific ProjectFlow project."""

    api_url, headers = get_config()

    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{api_url}/projects/{project_id}",
            headers=headers
        )

        response.raise_for_status()
        return response.json()


@mcp.tool()
async def list_tasks(project_id: str) -> dict:
    """List tasks belonging to a specific ProjectFlow project."""

    api_url, headers = get_config()

    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{api_url}/projects/{project_id}/tasks",
            headers=headers
        )

        response.raise_for_status()
        return response.json()


@mcp.tool()
async def create_task(
    project_id: str,
    title: str,
    description: str,
    priority: str
) -> dict:
    """Create a task inside a ProjectFlow project."""

    api_url, headers = get_config()

    payload = {
        "title": title,
        "description": description,
        "priority": priority
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{api_url}/projects/{project_id}/tasks",
            headers=headers,
            json=payload
        )

        response.raise_for_status()
        return response.json()