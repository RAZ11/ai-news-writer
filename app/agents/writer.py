from app.services.llm_services import llm

def writer(state):

    feedback = state.get("rewrite_feedback", "")

    prompt = f"""

you are a senior Bussiness Standard Journalist.

STRICT RULES:

1. Use ONLY information present in the Research section.
2. DO NOT add facts from your own knowledge.
3. DO NOT add statistics, forecasts, dates, organizations, GDP figures, RBI projections, IMF estimates, or economic claims unless explicitly present in Research.
4. If information is missing, omit it.
5. Do not make assumptions.
6. Do not invent facts.

Topic:
{state["topic"]}

Research:
{state["research"]}

Previous Fedback:
{feedback}

use the feedback if present

Write:
1. Headline
2. Exclusive Sammary
3. News Article


"""

    response = llm.invoke(prompt)

    return{
        "draft": response.content
    }