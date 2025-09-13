# === Python Modules ===
from typing import TypedDict, Literal, Optional, List

# === Answers Log ===
class AnswerLog(TypedDict):
    q: str
    ans: str
    eval: str
    score: int

# === Agent State ===
class AgentState(TypedDict):
    # === Unique ID ===
    session_id: str
    user_id: Optional[str]

    # === Difficulty (Adaptive) ===
    difficulty: int

    # === Question Count and Scores ===
    question_count: int
    scores: List[int]
    difficulties: List[int]

    # === Is there any need for clarification ===
    clarification_needed: bool
    clarifications_used: int    

    # === History ===
    answers_log: List[AnswerLog]

    # === Final Decision ===
    final_decision: Optional[Literal["pass", "fail", "review"]]