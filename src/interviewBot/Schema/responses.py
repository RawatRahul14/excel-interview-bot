# === Python Modules ===
from pydantic import BaseModel

## === Session ID ===
class SessionResponse(BaseModel):
    session_id: str