# === Python Modules ===
import streamlit as st
from typing import Dict , Any

## === Function to initialise the state session inside the Streamlit UI ===
def init_session():
    """
    Initialises the required state sessions
    """
    ### === Requierd State sessions ===
    sessions: Dict[str, Any] = {
        "messages": []
    }

    ### === Initialising using the for loop ===
    for key, value in sessions.items():
        if key not in st.session_state:
            st.session_state[key] = value