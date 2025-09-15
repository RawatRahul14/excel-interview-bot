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