from typing import TypedDict

class NewsState(TypedDict):
    topic: str

    search_results: str
    sources: list[str]

    research: str

    draft: str

    fact_check_report: str
    fact_check_status: str

    rewrite_feedbak: str
    retry_count: int

    final_article: str
