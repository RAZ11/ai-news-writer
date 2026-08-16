from app.services.llm_services import llm
from app.services.bedrock_services import bedrock_llm

def writer(state):

    feedback = state.get("rewrite_feedback", "")

    prompt = f"""

You are a senior Business Standard journalist.

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

Write like an experienced Business Standard reporter.

Use simple and direct financial journalism language.

Avoid AI-style phrases such as:
- underscores
- highlights
- signifies
- demonstrates
- robust
- strong tailwind
- pivotal
- transformative
- broader transition
- decisive reversal
- growing confidence
- market trajectory
- capital infusion
- investor appetite

Prefer factual reporting.

Example: Foreign Portfolio Investors signalled renewed confidence in the Indian market through a decisive capital infusion, reflecting a broader transition from caution to confidence.

Use:
- according to data
- analysts said
- market participants said
- the inflow comes after
- compared with
- the trend follows
- investors attributed
- data showed

Keep sentences short and natural.

Example: Foreign portfolio investors invested Rs 16,621 crore in Indian equities during the first half of August, extending their buying after a Rs 20,200-crore inflow in July.

Requirements:
- Strong headline
- 2-3 sentence standfirst
- Journalistic tone
- Historical context
- Explain why the event matters
- No bullet points
- No markdown
- Professional newspaper style
- 500-800 words

"""

    response = bedrock_llm.invoke(prompt)

    return{
        "draft": response.content
    }