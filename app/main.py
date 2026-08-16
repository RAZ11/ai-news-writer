from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.graph.workflow import graph
from app.schemas.news import NewsRequest, UpdateArticleRequest
from app.db.session import get_db
from app.services.article_service import save_article, get_article
from app.services.article_service import get_article_by_id, delete_article
from app.services.article_service import update_article

app = FastAPI(
    title="AI News Writer"
)

@app.get("/")
def home():
    return {
        "message": "AI News Writer v2 By Rajesh"
    }

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
        research=extract_text(result["research"]),
        article=extract_text(result["final_article"]),
        fact_check=extract_text(result["fact_check_report"]),
        title=result["title"],
        summary=result["summary"],
        category=result["category"],
        tags=",".join(result["tags"])

    )

    return {
        "id": saved_article.id,
        "topic": saved_article.topic,
        "article": saved_article.article,
        "title":saved_article.title,
        "summary":saved_article.summary,
        "category":saved_article.category,
        "tags":saved_article.tags
    }

@app.get("/get_article")
def get_article_api(db:Session = Depends(get_db)):

    articles = get_article(db)

    return articles


@app.get("/articles/{article_id}")
def get_aricle_by_id(article_id: int, db: Session = Depends(get_db)):

    return get_article_by_id(
        db, 
        article_id
    )

def extract_text(content):
    if isinstance(content, str):
        return content

    if isinstance(content, list):
        text_parts = []

        for item in content:
            if isinstance(item, dict) and item.get("type") == "text":
                text_parts.append(item.get("text", ""))

        return "\n".join(text_parts)

    return str(content)

# @app.put("/articles/{article_id}")
# def update_article(
#     article_id:int, 
#     request:UpdateArticleRequest, 
#     db:Session = Depends(get_db)
# ):

#     return update_article(
#         db,
#         article_id,
#         request.article
#     )


@app.delete("/delete_article/{article_id}")
def delete_article_by_id(article_id: int, db:Session = Depends(get_db)):

    deleted = delete_article(
        db, 
        article_id
    )

    return {
        "Article deleted" : deleted
    }

