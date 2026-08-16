from langgraph.graph import StateGraph, END
from app.schemas.state import NewsState

from app.agents.search_agent import search_agent
from app.agents.researcher import researcher
from app.agents.writer import writer
from app.agents.fact_checker import fact_checker, route_after_fact_check
from app.agents.editor import editor
from app.agents.publisher_agent import publisher_agent

builder = StateGraph(NewsState)
builder.add_node("search_agent", search_agent)
builder.add_node("researcher", researcher)
builder.add_node("writer", writer)
builder.add_node("fact_checker", fact_checker)
builder.add_node("editor", editor)
builder.add_node("publisher", publisher_agent)

builder.set_entry_point("search_agent")

builder.add_edge("search_agent", "researcher")
builder.add_edge("researcher", "writer")
builder.add_edge("writer", "fact_checker")

builder.add_conditional_edges(

    "fact_checker",
    route_after_fact_check,
    {
        "editor": "editor",
        "writer": "writer"

    }
)

builder.add_edge("editor","publisher")

builder.add_edge("publisher", END)


graph = builder.compile()
