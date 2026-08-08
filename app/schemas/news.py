from pydantic import BaseModel

class NewsRequest(BaseModel):
    topic: str