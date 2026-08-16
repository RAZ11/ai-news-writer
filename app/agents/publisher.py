
from app.services.llm_services import llm
from app.services.bedrock_services import bedrock_llm

import json

def publisher_agent(state):

    article = state["final_article"]

    prompt = f"""
    You are a news publisher.

    Based on the article:

    {article}

    Generate:

    1. Title
    2. Summary (5-6 lines)
    3. Category
    4. Tags

    Return JSON format.
    """

    response = llm.invoke(prompt)

    data = json.loads(response.content)

    return {
        "title": data["title"],
        "summary": data["summary"],
        "category": data["category"],
        "tags": data["tags"]
    }
