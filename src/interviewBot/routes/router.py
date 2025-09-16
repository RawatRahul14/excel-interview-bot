# === Python Modules ===


# === Custom Modules ===


# === AgentState ===
from interviewBot.agent_state import AgentState

# === Routes ===
## === Verification Route ===
async def is_verified(
        state: AgentState
) -> str:
    """
    Checks if the user id is verified or not
    """
    id_verified = state.get("verified")

    if id_verified:
        return "questions"

    else:
        return "error_handler"

## === Verification Error ===
async def ask_id(
        state: AgentState
) -> str:
    """
    Based on the number of verifications asks forid again
    """
    if state.get("verification_count") == 2:
        return "end_graph"

    else:
        return "user_verify_node"

## === Question Flow ===
async def is_question_done(
        state: AgentState
) -> str:
    """
    Checks whether the total number of questions are done or not
    """
    questions_done = state.get("question_count")

    if questions_done == 2:
        return "report"

    else:
        return "adaptive"