from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from graph.state import BlogState
from utils.prompts import WRITER_PROMPT
from utils.config import GROQ_API_KEY, MODEL_NAME, TEMPERATURE


def writer_agent(state: BlogState) -> BlogState:
    
    print("✍️ AGENT 3: CONTENT WRITER - Starting...")
    print(f"Writing blog post about: {state['topic']}")
    

    if not state["research_notes"]:
        print("   ❌ ERROR: No research notes found!")
        return {
            **state,
            "error_message": "Writer failed: No research notes available",
            "current_agent": "writer_error"
        }

    if not state["outline"]:
        print("❌ ERROR: No outline found!")
        return {
            **state,
            "error_message": "Writer failed: No outline available",
            "current_agent": "writer_error"
        }

    llm = ChatGroq(
        api_key=GROQ_API_KEY,
        model=MODEL_NAME,
        temperature=TEMPERATURE
    )

    prompt_text = WRITER_PROMPT.format(
        research_notes=state["research_notes"],
        outline=state["outline"]
    )

    print("📡 Sending writing request to AI (this may take a moment)...")
    response = llm.invoke([HumanMessage(content=prompt_text)])
    draft_content = response.content

    word_count = len(draft_content.split())
    print(f"✅ Draft written! Word count: ~{word_count} words")

    preview = draft_content[:200] + "..." if len(draft_content) > 200 else draft_content
    print(f"Preview: {preview}")

    return {
        **state,
        "draft_content": draft_content,
        "current_agent": "writer_done"
    }
