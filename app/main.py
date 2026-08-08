from fastapi import FastAPI
from app.graph.workflow import graph
from app.schemas.news import NewsRequest

app = FastAPI(
    title="AI News Writer"
)

@app.post("/generate_news")
def generate_news(request:NewsRequest):
    result = graph.invoke(
        {
            "topic": request.topic
        }
    )

    return {
        "topic": result["topic"],
        "article": result["final_article"],
        "fact_check": result["fact_check_report"]
    }