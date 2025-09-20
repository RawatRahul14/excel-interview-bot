# === Python Modules ===
from pydantic import BaseModel

## === Chatbot Requests ===
class ChatbotRequests(BaseModel):
    session_id: str
    user_input: str