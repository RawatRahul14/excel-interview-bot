# === AgentState ===
from interviewBot.agent_state import AgentState, AnswerLog

# === Agent Main Body ===
async def difficulty_adaptive(
        state: AgentState
) -> AgentState:
    """
    Updates the difficulty of the questions and also, updates the histories
    """
    state["difficulties"].append(state.get("difficulty"))

    return state