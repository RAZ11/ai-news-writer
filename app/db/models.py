from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import ARRAY

from app.db.database import Base


class NewsArticle(Base):

    __tablename__ = "news_articles"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(Text, nullable=True)
    topic = Column(Text, nullable=False)

    summary = Column(Text, nullable=True)
    category = Column(Text, nullable=True)

    tags = Column(ARRAY(Text), nullable=True)

    article = Column(Text, nullable=False)

    research = Column(Text)
    fact_check = Column(Text)

    model_used = Column(String(100), nullable=True)

    status = Column(
        String(50),
        nullable=False,
        default="draft"
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    published_at = Column(
        DateTime(timezone=True),
        nullable=True
    )
