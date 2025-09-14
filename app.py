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
        st.info(sidebar_detail)
        if st.session_state["start_interview"] == False:
            if st.button(
                label = "Start Interview"
            ):
                # === If session is not already created ===
                if st.session_state["session_id"] is None:
                    # === Flag to start the interview ===
                    st.session_state["start_interview"] = True

                    try:
                        # === Getting the Session_id from the backend ===
                        resp = requests.post(
                            url = f"{API_URL}/session_id",
                            timeout = 10
                        )

                        ## === Checking if the connection is made ===
                        if resp.status_code == 200:

                            ## === Changing the data into proper jsn format for easy data extraction ===
                            data = resp.json()

                            ## === Saving the session ID ===
                            st.session_state["session_id"] = data["session_id"]
                            st.success("✅ Session Started Successfully!")

                            ## === Saving the intro message ===
                            st.session_state.messages.append({
                                "role": "assistant",
                                "content": first_message
                            })

                            st.rerun()

                        else:
                            st.error(f"❌ Failed to start session: {resp.status_code}")

                    except Exception as e:
                        st.error(f"⚠️ Error connecting to backend: {e}")

                else:
                    st.warning("Interview already started.")

    for msg in st.session_state.messages:
        ## === Printing the user's message instantaneously ===
        if msg["role"] == "user":
            with st.chat_message("user"):
                st.markdown(msg["content"])

        ## === Using streaming for the assistant message ===
        elif msg["role"] == "assistant":
            with st.chat_message("assistant"):
                st.write_stream(stream_text(msg["content"]))

    ## === User Input ===
    user_input = st.chat_input("Type your answer here...")

    if user_input and st.session_state["start_interview"]:
        # Save user input
        st.session_state.messages.append({
            "role": "user",
            "content": user_input
        })

        # Mock bot reply (later: replace with FastAPI call)
        bot_reply = "Placeholder response from backend"
        st.session_state.messages.append({
            "role": "assistant",
            "content": bot_reply
        })

        st.rerun()


if __name__ == "__main__":
    main()
