from app.db.database import engine
from app.db.database import Base
from app.db.models import NewsArticle

Base.metadata.create_all(bind=engine)


print("Create table successfully")