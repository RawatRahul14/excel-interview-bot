# === Python Modules ===
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# === Custom Modules ===
from interviewBot.Schema.model_output import EvaluationAgentNode

# === AgentState ===
from interviewBot.agent_state import AgentState

# === Main Agent Body ===
async def evaluate(
        state: AgentState
) -> AgentState:
    """
    Agent to evaluate the user's answer against the expected answer,
    assign a score, adjust difficulty, and provide a short evaluation.
    """
    ## === Variables needed ===
    user_answer = state.get("answer_recieved")
    expected_answer = state.get("expected_answer")
    difficulty = state.get("difficulty")

    # === LLM Model ===
    llm_model = ChatOpenAI(
        model = "gpt-4o-mini",
        temperature = 0
    ).with_structured_output(EvaluationAgentNode)

    # === Prompt ===
    prompt = f"""
    You are an expert evaluator for an Excel interview.

    Your task is to compare the **Candidate's Answer** with the **Expected Answer** and provide a structured evaluation.

    Focus on:
        - Accuracy of the content
        - Completeness of the explanation
        - Use of correct Excel terminology
        - Clarity and relevance

    **Candidate's Answer**: {user_answer}
    **Expected Answer**: {expected_answer}
    **Current Difficulty**: {difficulty} out of 10

    Scoring Rules:  
        - Give a score between 0 and 10 (0 = completely wrong, 10 = perfect).  
        - Adjust difficulty for the next question:  
            * If score >= 8 -> increase difficulty by +1 (up to max 10).  
            * If score <= 4 -> decrease difficulty by -1 (down to min 1).  
            * Otherwise -> keep difficulty the same.  
        - Provide a **short, one-line evaluation** (e.g., "Good explanation with examples" or "Missed key details").  
    """

    response = await llm_model.ainvoke(prompt)

    ## === Updating the state ===
    state["difficulty"] = response.difficulty
    state["evaluation"] = response.evaluation
    state["got_score"] = response.score

    return state