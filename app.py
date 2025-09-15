# === Python Modules ===
import streamlit as st
import requests

# === Custom Modules ===
from interviewBot.utils.common import init_session
from interviewBot.utils.ui_streamer import stream_text

# === Details ===
from interviewBot.details import (
    sidebar_detail,
    first_message
)

# === FastAPI endpoint ===
API_URL = "http://127.0.0.1:8000"

# === Main Function ===
def main():
    """
    Main User Interface of the Bot
    """

    ## === Page Configurations ===
    st.set_page_config(
        page_title = "Excel Interview Bot",
        layout = "wide"
    )

    st.title("📊 AI-Powered Excel Interview Bot")

    ## === Initialising the sessions ===
    init_session()

    ## === Sidebar: Start Button ===
    with st.sidebar:
        ## === Information related to starting the interview ===
        st.info(sidebar_detail)

        # === If the interview is not started ===
        if not st.session_state["start_interview"]:

            ## === Button to start the interview ===
            if st.button(
                label = "🚀 Start Interview"
            ):
                ### === Recieving the Session ID from the Backend ===
                if st.session_state["session_id"] is None:

                    ### === Changing the flag to True for start_interview ===
                    st.session_state["start_interview"] = True

                    ### === Requesting the backend ===
                    try:
                        resp = requests.post(
                            url = f"{API_URL}/session_id",
                            timeout = 10
                        )

                        ### === If backend responsed properly ===
                        if resp.status_code == 200:
                            data = resp.json()

                            ### === Saving te session id in the session state ===
                            st.session_state["session_id"] = data["session_id"]

                            # === Adding intro to the messages ===
                            if not st.session_state["intro_shown"]:

                                ### === Appending for the first time ===
                                st.session_state.messages.append({
                                    "role": "assistant",
                                    "content": first_message
                                })

                                ### === Extra sessions ===
                                st.session_state["intro_shown"] = True
                                st.session_state["pending_stream"] = first_message

                            st.success("✅ Session Started Successfully!")
                            st.rerun()

                        else:
                            st.error(f"❌ Failed to start session: {resp.status_code}")

                    except Exception as e:
                        st.error(f"⚠️ Error connecting to backend: {e}")

                else:
                    st.warning("Interview already started.")

    ## === Chat Display ===
    for i, msg in enumerate(st.session_state.messages):
        with st.chat_message(msg["role"]):

            # === Streaming only the latest message from the bot ===
            if msg["role"] == "assistant" and msg["content"] == st.session_state["pending_stream"]:
                st.write_stream(stream_text(msg["content"]))
                st.session_state["pending_stream"] = None

            # === Displaying the user's reply normally ===
            else:
                st.markdown(msg["content"])

    ## === User Input ===
    user_input = st.chat_input("Type your answer here...")

    if user_input and st.session_state["start_interview"]:
        # Save user input
        st.session_state.messages.append({
            "role": "user",
            "content": user_input
        })

        # Generate assistant reply (placeholder now)
        bot_reply = "Placeholder response from backend"
        st.session_state.messages.append({
            "role": "assistant",
            "content": bot_reply
        })

        # === Saving the latest Bot message as the pending_stream ===
        st.session_state["pending_stream"] = bot_reply

        st.rerun()


if __name__ == "__main__":
    main()
