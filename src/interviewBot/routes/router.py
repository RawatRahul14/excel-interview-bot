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