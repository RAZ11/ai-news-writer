import os
from langchain_aws import ChatBedrockConverse

bedrock_llm = ChatBedrockConverse(
    model=os.getenv("BEDROCK_MODEL_ID"),
    region_name="us-east-1"
)


def generate_article(prompt: str):
    response = bedrock_llm.invoke(prompt)

    if isinstance(response.content, list):
        text_parts = []

        for item in response.content:
            if item.get("type") == "text":
                text_parts.append(item.get("text", ""))

        return "\n".join(text_parts)

    return str(response.content)