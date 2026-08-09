from sqlalchemy.orm import Session
from app.db.models import NewsArticle


def save_article(
        db: Session,
        topic:str,
        research:str,
        article:str,
        fact_check:str
):
    news_article = NewsArticle(
        topic=topic,
        research=research,
        article=article,
        fact_check=fact_check
    )
    db.add(news_article)

    db.commit()
    db.refresh(news_article)

    return news_article