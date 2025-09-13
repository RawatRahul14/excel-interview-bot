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
        "session_id": str(uuid.uuid4()),
        "user_id": None,

        # === Difficulty (Adaptive) ===
        "difficulty": 5,

        # === Question Count and Scores ===
        "question_count": 0,
        "scores": [],
        "difficulties": [5],

        # === Is there any need for clarification ===
        "clarification_needed": False,
        "clarifications_used": 0,

        # === History ===
        "answers_log": [],

        # === Final Decision ===
        "final_decision": None
    }

    return new_state