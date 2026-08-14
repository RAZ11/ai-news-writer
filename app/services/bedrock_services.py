from langchain_aws import ChatBedrockConverse

bedrock_llm = ChatBedrockConverse(
    model="deepseek.v3.2",
    region_name="us-east-1"
)

def generate_article(prompt: str):
    response = bedrock_llm.invoke(prompt)
    return response.content