from pydantic import BaseModel

class NewsRequest(BaseModel):
    topic: str




class UpdateArticleRequest(BaseModel):
    article:str