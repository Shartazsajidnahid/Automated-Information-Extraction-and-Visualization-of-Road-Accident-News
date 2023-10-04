from pydantic import BaseModel

class NewsArticle(BaseModel):
    id: int
    title: str
    content: str