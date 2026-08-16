
from app.services.llm_services import llm
from app.services.bedrock_services import bedrock_llm

import json

def publisher_agent(state):

    article = state["final_article"]

    prompt = f"""
    You are a news publisher.

    Based on the article:

    {article}

        
    Write the article in Business Standard style.

    Requirements:
    - Strong headline
    - 2-3 sentence standfirst
    - Journalistic tone
    - Historical context
    - Explain why the event matters
    - No bullet points
    - No markdown
    - Professional newspaper style
    - 300-500 words

   
    Return ONLY valid JSON.

    Generate:

        1. Title
        2. Summary (5-6 lines)
        3. Category
        4. Tags

    Example:

    {{
    "title": "Sample Title",
    "summary": "500-800 word article",
    "category": "Business",
    "tags": ["stock market", "finance"]
    }}

    Do not return markdown.
    Do not return explanations.
    Do not return code fences.
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

    print("PUBLISHER_DATA:", data)

    return {
        "title": data.get("title") or data.get("headline", ""),
        "summary": data.get("summary", ""),
        "category": data.get("category", ""),
        "tags": data.get("tags", [])
    }
