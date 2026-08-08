from app.services.search_service import search_news

def search_agent(state):

    print("Search Agent:")

    topic = state["topic"]

    results = search_news(topic)

    search_text = ""

    for item in results:
        search_text += f"""

    Title: 
    {item['title']}

    Content:
    {item['content']}

    Sourch:
    {item['url']}

    ------------------------------
    """

    sources = [item["url"] for item in results]

    print("\n=== SEARCH RESULT OUTPUT ===")
    print(search_text)

    return {
        "search_results": search_text,
        "sources": sources
    }