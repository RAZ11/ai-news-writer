import os
from tavily import TavilyClient

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)

def search_news(query: str):

    print("search News:")
    response = client.search(
        query=query,
        next_result=5
    )

    results = []

    for item in response["results"]:
        results.append(
            {
                "title": item["title"],
                "content": item["content"],
                "url":item["url"]
            }
        )

        return results

