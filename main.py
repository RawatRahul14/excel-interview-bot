# === Python Modules ===
from fastapi import FastAPI

# === Custom Modules ===
from interviewBot.utils.common import (
    get_session_id
)

# === Response Schemas ===
from interviewBot.Schema.responses import (
    SessionResponse
)

# === FastAPI endpoints ===
app = FastAPI()

## === Sending Session id ===
@app.post("/session_id", response_model = SessionResponse)
async def session_id():
    """
    Generates Session ID used for the thread id in Graph
    """
    session_id = get_session_id()

    return SessionResponse(
        session_id = session_id
    )