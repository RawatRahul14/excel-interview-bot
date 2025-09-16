# === Python Modules ===
from langchain_openai import ChatOpenAI
import json

# === Custom Modules ===
from interviewBot.Schema.model_output import ReportAgentNode

# === AgentState ===
from interviewBot.agent_state import AgentState

# === Main Agent Body ===
async def report(
        state: AgentState
) -> AgentState:
    """
    Agent to create a downloadable report of the user
    """
    # === Variables needed ===
    answer_logs = state.get("answers_log")

    answer_logs_json = json.dumps(
        answer_logs,
        indent = 2
    )

    # === LLM model ===
    llm_model = ChatOpenAI(
        model = "gpt-4o-mini",
        temperature = 0
    ).with_structured_output(ReportAgentNode)

    prompt = f"""
    You are a professional interviewer generating a **structured interview report**.
    The candidate has completed an Excel interview.
    Below are the detailed logs of the candidate's answers in JSON format:

    logs = {answer_logs_json}

    Your task:
        1. Provide a concise **overall summary** of the candidate's performance.  
        2. Highlight **strengths** (topics where candidate did well).  
        3. Highlight **weaknesses or improvement areas**.
        4. Comment on the candidate's **progression of difficulty vs scores** (if they improved, declined, or stayed consistent).  

        Also, you need to specifically tell whether the candidate is passed or failed or needs a review.
    """

    response = await llm_model.ainvoke(prompt)

    state["report"] = response.report
    state["final_decision"] = response.final_decision

    return state