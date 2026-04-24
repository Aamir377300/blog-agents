from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from graph.state import BlogState
from utils.prompts import REVIEWER_PROMPT
from utils.config import GROQ_API_KEY, MODEL_NAME, TEMPERATURE


def reviewer_agent(state: BlogState) -> BlogState:
    
    print("🔎 AGENT 4: QUALITY REVIEWER - Starting...")
    print(f"Reviewing blog post about: {state['topic']}")
    

    if not state["draft_content"]:
        print("❌ ERROR: No draft content found!")
        return {
            **state,
            "error_message": "Reviewer failed: No draft content available",
            "current_agent": "reviewer_error"
        }

    llm = ChatGroq(
        api_key=GROQ_API_KEY,
        model=MODEL_NAME,
        temperature=0.3
    )

    prompt_text = REVIEWER_PROMPT.format(draft_content=state["draft_content"])

    print("📡 Sending review request to AI...")
    response = llm.invoke([HumanMessage(content=prompt_text)])
    final_content = response.content

    word_count = len(final_content.split())
    print(f"✅ Review complete! Final word count: ~{word_count} words")
    print("🎉 Blog post is ready!")

    return {
        **state,
        "final_content": final_content,
        "current_agent": "complete"
    }
