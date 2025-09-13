# === Python Modules ===
import streamlit as st

# === Custom Modules ===
from interviewBot.utils.common import init_session

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

    ## === Chat Display ===
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    ## === User Input ===
    user_input = st.chat_input("Type your answer here...")

    if user_input:
        ### === Save user input ===
        st.session_state.messages.append({
            "role": "user",
            "content": user_input
        })

        ### === Mock bot reply (later async FastAPI call) ===
        bot_reply = "Placeholder"
        st.session_state.messages.append({
            "role": "assistant",
            "content": bot_reply
        })

        # === Refresh UI ===
        st.rerun()

if __name__ == "__main__":
    main()