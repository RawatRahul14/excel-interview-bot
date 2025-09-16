# === Python Modules ===
from typing import TypedDict, Literal, Optional, List

# === Answers Log ===
class AnswerLog(TypedDict):
    q: str
    e_ans: str
    ans: str
    eval: str
    score: int

# === Agent State ===
class AgentState(TypedDict):
    # === Unique ID ===
    user_id: Optional[str]
    verified: Optional[bool]
    verification_count: int

    # === Difficulty (Adaptive) ===
    difficulty: int

    # === Question Count and Scores ===
    question: Optional[str]
    expected_answer: Optional[str]
    answer_recieved: Optional[str]
    used_topics: List[str]
    question_count: int
    got_score: Optional[int]
    scores: List[int]
    difficulties: List[int]
    evaluation: Optional[str]

    # === Is there any need for clarification ===
    clarification_needed: bool
    clarifications_used: int    

    # === History ===
    answers_log: List[AnswerLog]

    # === Final Decision ===
    report: Optional[str]
    final_decision: Optional[Literal["pass", "fail", "review"]]
    final_message: Optional[str]