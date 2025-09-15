# === AgentState ===
from interviewBot.agent_state import AgentState

# === Main Agent Body ===
async def error_handler(
        state: AgentState
) -> AgentState:
    """
    This will work as a passthrough node
    """
    return state