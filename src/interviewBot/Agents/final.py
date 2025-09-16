# === Python Modules ===
import os
from dotenv import load_dotenv

# === Components ===
from interviewBot.components.report_upload import upload_report

# === Agent State ===
from interviewBot.agent_state import AgentState

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
DB_NAME_UPLOAD = os.getenv("DB_NAME_UPLOAD")
COLLECTION_NAME_UPLOAD = os.getenv("COLLECTION_NAME_UPLOAD")

# === Main Agent Body ===
async def finalizer(
        state: AgentState
) -> AgentState:
    """
    Uploads the Candidates Result and answer logs on MongoDB.
    """
    # === Extract required values from state ===
    user_id = state.get("user_id")
    answers_log = state.get("answers_log")
    report = state.get("report")
    final_decision = state.get("final_decision")

    # === Upload to MongoDB ===
    await upload_report(
        user_id = user_id,
        answers_log = answers_log,
        report = report,
        final_decision = final_decision,
        mongo_uri = MONGODB_URI,
        db_name = DB_NAME_UPLOAD,
        collection_name = COLLECTION_NAME_UPLOAD
    )

    # === Final Message to the user ===
    state["final_message"] = "Your report and result have been uploaded to the system, based on your result HR will contact within 2-3 working days. Thank You."

    return state