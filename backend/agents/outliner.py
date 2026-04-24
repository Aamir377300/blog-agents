from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from graph.state import BlogState
from utils.prompts import OUTLINER_PROMPT
from utils.config import GROQ_API_KEY, MODEL_NAME, TEMPERATURE


def outliner_agent(state: BlogState) -> BlogState:
    
    print("📋 AGENT 2: CONTENT OUTLINER - Starting...")
    print(f"Working with research on: {state['topic']}")
    

    if not state["research_notes"]:
        print("❌ ERROR: No research notes found!")
        return {
            **state,
            "error_message": "Outliner failed: No research notes available",
            "current_agent": "outliner_error"
        }

    llm = ChatGroq(
        api_key=GROQ_API_KEY,
        model=MODEL_NAME,
        temperature=TEMPERATURE
    )

    prompt_text = OUTLINER_PROMPT.format(research_notes=state["research_notes"])

    print("📡 Sending outline request to AI...")
    response = llm.invoke([HumanMessage(content=prompt_text)])
    outline = response.content

    preview = outline[:200] + "..." if len(outline) > 200 else outline
    print(f"✅ Outline created! Preview: {preview}")

    return {
        **state,
        "outline": outline,
        "current_agent": "outliner_done"
    }
