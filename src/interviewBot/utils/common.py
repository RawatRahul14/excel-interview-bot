# === Python Modules ===
import streamlit as st
from typing import Dict , Any
from pathlib import Path
import uuid
import yaml
import os

## === Function to initialise the state session inside the Streamlit UI ===
def init_session():
    """
    Initialises the required state sessions
    """
    ### === Requierd State sessions ===
    sessions: Dict[str, Any] = {
        "messages": [],
        "start_interview": False,
        "session_id": None,
        "intro_shown": False,
        "pending_stream": None
    }

    ### === Initialising using the for loop ===
    for key, value in sessions.items():
        if key not in st.session_state:
            st.session_state[key] = value

## === Function to get the session id unique for each person ===
def get_session_id() -> str:
    """
    Creates a unique session id for each person
    """
    id: str = str(uuid.uuid4())

    return id

def load_yaml(
        path: Path
):
    """
    Loads the yaml file
    """
    # === Load Topics from YAML ===
    with open(
        path,
        "r",
        encoding = "utf-8"
    ) as f:
        topics_data = yaml.safe_load(f)["excel_topics"]

    return topics_data