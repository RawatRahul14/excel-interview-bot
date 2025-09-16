# === Python Module ===
from pydantic import BaseModel, Field
from typing import Literal

# === Question Agent Node ===
class QuestionAgentNode(BaseModel):
    question: str = Field(
        description = "Excel question created by the model."
    )

    answer: str = Field(
        description = "Answer formed by the model on which the user's answer will be evaluated."
    )

# === Evaluation Agent Node ===
class EvaluationAgentNode(BaseModel):
    score: int = Field(
        description = "Evaluation score a person got by evaulating their answer with the expected asnwer."
    )

    difficulty: int = Field(
        description = "What difficulty should the person get for the next question based on the last asnwer."
    )

    evaluation: str = Field(
        description = "A single line evaluation of the user's answer."
    )

# === Report Maker Node ===
class ReportAgentNode(BaseModel):
    report: str = Field(
        description = "Report made by the agent based on the answer logs of the user."
    )

    final_decision: Literal["pass", "fail", "review"] = Field(
        description = "Whether the person is failed/passed or needs review"
    )