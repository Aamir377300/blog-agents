from langgraph.graph import StateGraph, END, START
from graph.state import BlogState
from agents.researcher import researcher_agent
from agents.outliner import outliner_agent
from agents.writer import writer_agent
from agents.reviewer import reviewer_agent


def create_workflow():
    print("🔧 Building workflow graph...")

    graph = StateGraph(BlogState)

    graph.add_node("researcher", researcher_agent)
    graph.add_node("outliner", outliner_agent)
    graph.add_node("writer", writer_agent)
    graph.add_node("reviewer", reviewer_agent)

    print("✅ Added 4 agent nodes to graph")

    graph.add_edge(START, "researcher")
    graph.add_edge("researcher", "outliner")
    graph.add_edge("outliner", "writer")
    graph.add_edge("writer", "reviewer")
    graph.add_edge("reviewer", END)

    print("✅ Connected all nodes: START→Researcher→Outliner→Writer→Reviewer→END")

    app = graph.compile()

    print("✅ Workflow compiled and ready!")

    return app


def run_workflow(topic: str) -> BlogState:
    from graph.state import create_initial_state

    initial_state = create_initial_state(topic)
    app = create_workflow()

    print(f"\n🚀 Starting Multi-Agent Blog Post Generator")
    print(f"Topic: '{topic}'")
    print(f"This will run 4 agents in sequence...\n")

    final_state = app.invoke(initial_state)

    return final_state
