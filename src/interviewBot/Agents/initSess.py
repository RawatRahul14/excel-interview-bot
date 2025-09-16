# === Python Modules ===
import uuid

# === AgentState ===
from interviewBot.agent_state import AgentState

# === Main Body ===
async def init_sess(
        state: AgentState
) -> AgentState:
    """
    Initializes the basic states for running the graph
    """

    new_state: AgentState = {
        # === Unique ID ===
        "user_id": None,
        "verified": None,
        "verification_count": 0,

        # === Difficulty (Adaptive) ===
        "difficulty": 5,

        # === Question Count and Scores ===
        "used_topics": [],
        "question": None,
        "expected_answer": None,
        "answer_recieved": None,
        "question_count": 0,
        "got_score": None,
        "scores": [],
        "difficulties": [5],
        "evaluation": None,

        # === Is there any need for clarification ===
        "clarification_needed": False,
        "clarifications_used": 0,

        # === History ===
        "answers_log": [],

        # === Final Decision ===
        "report": None,
        "final_decision": None
    }

    return new_state