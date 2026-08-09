from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.graph.workflow import graph
from app.schemas.news import NewsRequest
from app.db.session import get_db
from app.services.article_service import save_article

app = FastAPI(
    title="AI News Writer"
)

@app.post("/generate_news")
def generate_news(request:NewsRequest, db:Session = Depends(get_db)):

    result = graph.invoke(
        {
            "topic": request.topic
        }
    )
    print("RAZ:", result)
    saved_article = save_article(
        db=db,
        topic=result['topic'],
        research=str(result['research']),
        article=str(result['final_article']),
        fact_check=str(result['fact_check_report'])

    )

    return {
        "id": saved_article.id,
        "topic": saved_article.topic,
        "article": saved_article.article
    }