from db.database import engine
from db.database import Base
from db.models import NewsArticle

Base.metadata.create_all(bind=engine)


print("Create table successfully")