from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from graph.state import BlogState
from utils.prompts import RESEARCHER_PROMPT
from utils.config import GROQ_API_KEY, MODEL_NAME, TEMPERATURE


def researcher_agent(state: BlogState) -> BlogState:
    
    print("🔍 AGENT 1: TOPIC RESEARCHER - Starting...")
    print(f"Topic: {state['topic']}")
    

    llm = ChatGroq(
        api_key=GROQ_API_KEY,
        model=MODEL_NAME,
        temperature=TEMPERATURE
    )

    prompt_text = RESEARCHER_PROMPT.format(topic=state["topic"])

    print("📡 Sending research request to AI...")
    response = llm.invoke([HumanMessage(content=prompt_text)])
    research_notes = response.content

    preview = research_notes[:200] + "..." if len(research_notes) > 200 else research_notes
    print(f"✅ Research complete! Preview: {preview}")

    return {
        **state,
        "research_notes": research_notes,
        "current_agent": "researcher_done"
    }
