# === Python Modules ===
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# === Custom Modules ===
from interviewBot.Schema.model_output import QuestionAgentNode

# === Components ===
from interviewBot.components.topic import get_topic

# === AgentState ===
from interviewBot.agent_state import AgentState

load_dotenv()

# === Main Agent Body ===
async def question(
        state: AgentState
) -> AgentState:
    """
    Agent to creates Excel Questions for the user based on the difficulty
    """
    # === Variables needed ===
    difficulty = state.get("difficulty")
    used_topics = state.get("used_topics")

    # === Getting the Topic Description ===
    topic_name, topic_description, used_topics = await get_topic(used_topics)

    llm_model = ChatOpenAI(
        model = "gpt-4o-mini",
        temperature = 0
    ).with_structured_output(QuestionAgentNode)

    prompt = f"""
    You are an AI Excel Interviewer.  
    Your task is to generate ONE interview-style Excel question with its correct answer.  

    Context:  
    - Topic's Name: "{topic_name}"
    - Topic's Description: "{topic_description}"(this is the exact area of focus for the question).  
    - Knowledge Level: {difficulty} (1 = beginner-level knowledge, 10 = expert-level knowledge).  

    Instructions:  
    1. Create a question strictly related to the given topic. Do not drift outside the topic.  
    2. Align the question complexity with the knowledge level:  
        - Levels 1-3 → Beginner knowledge: definitions, basic formulas, simple operations.  
        - Levels 4-6 → Intermediate knowledge: combining formulas, practical use cases, applied problem-solving.  
        - Levels 7-10 → Advanced knowledge: complex scenarios, multi-step problem-solving, nested formulas, pivot tables, advanced data analysis, VBA/macros, or optimization tasks.  
    3. Phrase the question exactly as an interviewer would ask in a real Excel interview.  
    4. After the question, provide the **correct answer** in a clear, step-by-step explanation or formula. Answer in only 2-3 lines.  
    """

    response = await llm_model.ainvoke(prompt)

    ## === Saving the outputs ===
    state["used_topics"] = used_topics
    state["question_count"] += 1
    state["question"] = response.question
    state["expected_answer"] = response.answer

    return state