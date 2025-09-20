# === Python Modules ===
from pydantic import BaseModel

## === Session ID ===
class SessionResponse(BaseModel):
    session_id: str
    first_message_verification: str

## === Chatbot reply ===
class ChatbotResponse(BaseModel):
    reply: str