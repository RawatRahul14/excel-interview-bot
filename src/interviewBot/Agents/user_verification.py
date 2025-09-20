# === Python Modules ===
import os
from langgraph.types import interrupt
from dotenv import load_dotenv

# === Agent State ===
from interviewBot.agent_state import AgentState

# === Components ===
from interviewBot.components.verification import verify_id

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
DB_NAME_VERIFICATION = os.getenv("DB_NAME_VERIFICATION")
COLLECTION_NAME_VERIFICATION = os.getenv("COLLECTION_NAME_VERIFICATION")


# === Main Node Body for Interrupt ===
async def user_verify_interrupt(
        state: AgentState
) -> AgentState:
    """
    Interrupts the user to get the user ID or email ID.
    If the user_id is already present in state, skip the interrupt.
    """

    # === To skip the interrupt if already present ===
    if state.get("user_id") and state["verified"] == True:
        return state

    if state.get("verification_count") == 0:
        interrput_message = "🔑 Before we begin, please enter your **Email ID** or **Employee ID** to verify yourself.\n\n✅ You'll have 2 attempts."

    else:
        interrput_message = "Last chance: Enter either your Email ID or Employee ID correctly."

    # === HITL Pause ===
    user_id = interrupt(
        {
            "message": (
                f"{interrput_message}"
            ),
            "interrupt_type": "verification",
            "field": "user_id"
        }
    )

    # === When resumed, `user_id` will be the value from Command(resume=<value>) ===
    state["user_id"] = user_id
    return state


# === Main Node Body for Verification ===
async def user_verify(
        state: AgentState
) -> AgentState:
    """
    Verifies whether the ID is valid or not.
    """
    user_id = state.get("user_id", "").strip()

    # Initialize count if missing
    state["verification_count"] = state.get("verification_count", 0)

    if user_id:
        verification_flag: str = await verify_id(
            user_id = user_id,
            mongo_uri = MONGODB_URI,
            db_name = DB_NAME_VERIFICATION,
            collection_name = COLLECTION_NAME_VERIFICATION
        )

        state["verified"] = verification_flag == "True"
        state["verification_count"] += 1
    else:
        state["verified"] = False

    return state
