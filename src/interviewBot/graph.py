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

# === Nodes ===
## === State Initializer ===
from interviewBot.Agents.initSess import init_sess

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
        "init_sess",
        RunnableLambda(init_sess).with_config(
            {
                "run_async": True
            }
        )
    )

    # === Edges ===

    ## === Entry Point ===
    workflow.set_entry_point("init_sess")

    ## === Connections ===
    workflow.add_edge("init_sess", END)

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