# === Python Modules ===
from langgraph.types import interrupt

# === Agent State ===
from interviewBot.agent_state import AgentState

# === Main Node Body for Interrupt to get answer from the user ===
async def get_answer(
        state: AgentState
) -> AgentState:
    """
    Interrupts the user to get the Answer.
    """
    # === To skip the interrupt if already present ===
    if state.get("answer_recieved"):
        return state

    # === HITL pause ===
    user_answer = interrupt(
        {
            "message": (
                f"{state.get('question')}"
            ),
            "interrupt_type": "qna",
            "field": "answer_recieved"
        }
    )

    state["answer_recieved"] = user_answer
    return state