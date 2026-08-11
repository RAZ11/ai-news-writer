from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy import DateTime
from sqlalchemy.sql import func

from app.db.database import Base

class NewsArticle(Base):

    __tablename__ = "news_articles"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    topic = Column(Text, nullable=False)
    research = Column(Text)
    article = Column(Text, nullable=False)
    fact_check = Column(Text)
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    


