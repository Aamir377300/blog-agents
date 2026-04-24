from typing import TypedDict


class BlogState(TypedDict):
    topic: str
    research_notes: str
    outline: str
    draft_content: str
    final_content: str
    current_agent: str
    error_message: str


def create_initial_state(topic: str) -> BlogState:
    return BlogState(
        topic=topic,
        research_notes="",
        outline="",
        draft_content="",
        final_content="",
        current_agent="starting",
        error_message=""
    )
