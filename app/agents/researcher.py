
from app.services.llm_services import llm
from app.services.bedrock_services import bedrock_llm

def researcher(state):


    prompt = f"""

    You are a senior business analyst.
    
    Topic: 
    {state['topic']}

    Search Results:
    {state['search_results']}
    
    Create structured research notes.

    Include:

    1. Background
    2. Key Facts
    3. Market Impact
    4. Risks
    5. Opportunities

    """

    response = bedrock_llm.invoke(prompt)
    
    print("\n=== RESEARCH OUTPUT ===")
    print(response)

    return {"research": response.content}
