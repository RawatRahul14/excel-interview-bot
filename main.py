# === Python Modules ===
from fastapi import FastAPI
from contextlib import asynccontextmanager
from langgraph.types import Command

# === Custom Modules ===
from interviewBot.utils.common import (
    get_session_id
)

# === Graph ===
from interviewBot.graph import build_graph

# === Requests Schema ===
from interviewBot.Schema.request import (
    ChatbotRequests
)

# === Response Schemas ===
from interviewBot.Schema.responses import (
    SessionResponse,
    ChatbotResponse
)

## === Startup event ===
@asynccontextmanager
async def lifespan(
    app: FastAPI
):
    """
    Initiates the graph
    """
    print("Graph Init.")
    # === Start up ===
    app.state.graph = await build_graph()

    yield

    # === Shutdown ===
    print("App shutting down.")

# === FastAPI endpoints ===
app = FastAPI(
    title = "Excel Interview ChatBot",
    lifespan = lifespan
)

## === Sending Session id ===
@app.post("/session_id", response_model = SessionResponse)
async def session_id():
    """
    Generates Session ID used for the thread id in Graph
    """
    ## === Session Id ===
    session_id = get_session_id()

    ## === First Interrupt ===
    graph = app.state.graph
    result = await graph.ainvoke(
        {},
        config = {
            "configurable": {
                "thread_id": session_id
            }
        }
    )

    ## === Extracting the message ===
    message = result["__interrupt__"][0].value

    return SessionResponse(
        session_id = session_id,
        first_message_verification = message.get("message")
    )

## === User Inputs ===
@app.post("/qna", response_model = ChatbotResponse)
async def start_qna(
    payload: ChatbotRequests
):
    """
    Accepts the user's message and reply appropriately
    """
    ## === Extracts the needed variables ===
    session_id = payload.session_id
    user_input = payload.user_input

    ## === Resuming the graph after the interrupts ===
    graph = app.state.graph

    result = await graph.ainvoke(
        Command(resume = user_input),
        config = {
            "configurable": {
                "thread_id": session_id
            }
        }
    )

    ## === Extracting the Message ===
    message = result["__interrupt__"][0].value

    return ChatbotResponse(
        reply = message.get("message")
    )