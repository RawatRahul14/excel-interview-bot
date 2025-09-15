# === Python Module ===
from pydantic import BaseModel, Field

# === Question Agent Node ===
class QuestionAgentNode(BaseModel):
    question: str = Field(
        description = "Excel question created by the model."
    )

    answer: str = Field(
        description = "Answer formed by the model on which the user's answer will be evaluated."
    )