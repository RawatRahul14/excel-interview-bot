# === Python Modules ===
import os
from langgraph.graph.state import StateGraph
from langgraph.graph import END
from langchain_core.runnables import RunnableLambda
from langgraph.checkpoint.mongodb import AsyncMongoDBSaver
from pymongo import AsyncMongoClient
from dotenv import load_dotenv

# === Custom Modules ===
from interviewBot.agent_state import AgentState

# === Routes ===
from interviewBot.routes.router import (
    is_verified,
    ask_id
)

# === Nodes ===
## === State Initializer ===
from interviewBot.Agents.initSess import init_sess

## === Verification ===
from interviewBot.Agents.user_verification import (
    user_verify_interrupt,
    user_verify
)

## === Question Node ===
from interviewBot.Agents.question_maker import question

## === Error Handler ===
from interviewBot.Agents.error import error_handler

## === Recieving answers from the user ===
from interviewBot.Agents.answers import get_answer

## === Evaluator ===
from interviewBot.Agents.evaluate import evaluate

load_dotenv()

# === Env Imports ===
MONGODB_URI = os.getenv("MONGODB_URI")
DB_NAME = os.getenv("DB_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

def build_workflow():
    """
    Builds the Workflow Structure (without checkpointer)
    """
    # === Initializing the graph flow with Agent State ===
    workflow = StateGraph(AgentState)

    # === Nodes ===

    ## === Initializing the Session ===
    workflow.add_node(
        "init_sess_node",
        RunnableLambda(init_sess).with_config(
            {
                "run_async": True
            }
        )
    )

    ## === Verification Interrrupt ===
    workflow.add_node(
        "user_verify_interrupt_node",
        RunnableLambda(user_verify_interrupt).with_config(
            {
                "run_async": True
            }
        )
    )

    ## === Verification Node ===
    workflow.add_node(
        "user_verify_node",
        RunnableLambda(user_verify).with_config(
            {
                "run_async": True
            }
        )
    )

    ## === Creating questions ===
    workflow.add_node(
        "questions_node",
        RunnableLambda(question).with_config(
            {
                "run_async": True
            }
        )
    )

    ## === Error Handler Node ===
    workflow.add_node(
        "error_handler_node",
        RunnableLambda(error_handler).with_config(
            {
                "run_async": True
            }
        )
    )

    ## === get_answer Node ===
    workflow.add_node(
        "get_answer_node",
        RunnableLambda(get_answer).with_config(
            {
                "run_async": True
            }
        )
    )

    ## === Ealuation Node ===
    workflow.add_node(
        "evaluate_node",
        RunnableLambda(evaluate).with_config(
            {
                "run_async": True
            }
        )
    )

    # === Edges ===

    ## === Entry Point ===
    workflow.set_entry_point("init_sess_node")

    ## === Connections ===
    workflow.add_edge("init_sess_node", "user_verify_interrupt_node")
    workflow.add_edge("user_verify_interrupt_node", "user_verify_node")
    workflow.add_conditional_edges(
        "user_verify_node",
        is_verified,
        {
            "questions": "questions_node",
            "error_handler": "error_handler_node"
        }
    )

    workflow.add_conditional_edges(
        "error_handler_node",
        ask_id,
        {
            "end_graph": END,
            "user_verify_node": "user_verify_interrupt_node"
        }
    )

    workflow.add_edge("questions_node", "get_answer_node")
    workflow.add_edge("get_answer_node", "evaluate_node")

    return workflow


async def build_graph():
    """
    Builds and Compiles the Graph Architecture with MongoDB Checkpointer
    """
    workflow = build_workflow()

    # === MongoClient ===
    mongo_client = AsyncMongoClient(MONGODB_URI)
    checkpointer = AsyncMongoDBSaver(
        client = mongo_client,
        db_name = DB_NAME,
        checkpoint_collection_name = COLLECTION_NAME
    )

    return workflow.compile(checkpointer = checkpointer)