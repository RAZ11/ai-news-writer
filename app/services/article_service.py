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


def get_article(db: Session):

    return db.query(
        NewsArticle
    ).all()


def get_article_by_id(db:Session, article_id:int):

    return(
        db.query(NewsArticle)
        .filter(
            NewsArticle.id == article_id
        )
        .first()
    )


def update_article(db, article_id: int, article: str):

    news_article = (
        db.query(NewsArticle)
        .filter(NewsArticle.id == article_id)
        .first()
    )

    if not news_article:
        return None

    news_article.article = article

    db.commit()

    db.refresh(news_article)

    return news_article


def delete_article(db, article_id: int):

    news_article = (
        db.query(NewsArticle)
        .filter(NewsArticle.id == article_id)
        .first()
    )

    if not news_article:

        return None
    db.delete(news_article)
    db.commit()

    return True