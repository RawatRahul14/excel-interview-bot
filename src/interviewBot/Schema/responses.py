# === Python Modules ===
from pydantic import BaseModel

## === Session ID ===
class SessionResponse(BaseModel):
    session_id: str
    first_message_verification: str

## === Verifcation ===
class VerificationResponse(BaseModel):
    verification_message: str