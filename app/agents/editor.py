from app.services.llm_services import llm
from app.services.bedrock_services import bedrock_llm


def editor(state):
    prompt = f"""
You are a professional newspaper editor.

Return ONLY the final polished article.

Do NOT include:
- Explanations
- Comments
- "Here is the revised article"
- Improvement notes
- Markdown separators
- *, **, ###

Article:
{state['draft']}

Sources:
{state['sources']}

Append a Sources section.

"""

    response = bedrock_llm.invoke(prompt)

    return{
        "final_article": response.content
    }