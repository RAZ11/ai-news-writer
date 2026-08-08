from app.services.llm_services import llm


def fact_checker(state):

    retry_count = state.get("retry_count", 0) + 1
    
    print("=== FACT CHECKER STARTED ===")

    prompt = f"""

    Research:
    {state['research']}

    Article:
    {state['draft']}
    
    Check whether every claim in the article is supported by the research.

    Return:

    STATUS: PASS

    or 

    STATUS: FAIL

    Also provide corrections.

    """

    print("Calling Gemini...")

    response = llm.invoke(prompt)

    print("Gemini response received")


    result = response.content

    status = "FAIL"

    if "STATUS: PASS" in result:
        status = "PASS"

    return{
        "fact_check_status": status,
        "fact_check_report": result,
        "rewrite_feedback": result,
        "retry_count": retry_count
    }


def route_after_fact_check(state):
    if state["fact_check_status"] == "PASS":

        return "editor"

    if state.get("retry_count", 0) >= 2:
        return "editor"

    return "writer"


