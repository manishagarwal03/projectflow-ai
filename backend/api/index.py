"""
Vercel serverless function entry point for FastAPI.
Strips /api prefix from requests before passing to FastAPI app.
"""
import sys
from pathlib import Path

# Add backend directory to path
backend_path = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(backend_path))

from app.main import app as fastapi_app


class StripAPIPrefix:
    """ASGI middleware to strip /api prefix from request paths."""
    
    def __init__(self, app):
        self.app = app
    
    async def __call__(self, scope, receive, send):
        if scope["type"] == "http":
            path = scope["path"]
            if path.startswith("/api"):
                scope["path"] = path[4:] or "/"
                scope["raw_path"] = scope["path"].encode("utf-8")
        
        await self.app(scope, receive, send)


# Wrap FastAPI app with middleware to strip /api prefix
app = StripAPIPrefix(fastapi_app)

# Vercel expects 'app' or 'handler' export
handler = app
