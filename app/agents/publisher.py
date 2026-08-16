
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

    content = response.content

    if isinstance(content, str):
        json_text = content

    elif isinstance(content, list):
        json_text = ""

        for item in content:
            if isinstance(item, dict) and item.get("type") == "text":
                json_text += item.get("text", "")

    else:
        raise ValueError(f"Unexpected response type: {type(content)}")

    print("JSON_TEXT:", json_text)

    data = json.loads(json_text)

    return {
        "title": data["title"],
        "summary": data["summary"],
        "category": data["category"],
        "tags": data["tags"]
    }
