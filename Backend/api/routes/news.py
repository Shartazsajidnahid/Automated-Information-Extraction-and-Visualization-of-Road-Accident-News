from fastapi import APIRouter
from ..controllers.news import scrape_all
from ..controllers.dummynews import dummy_news, get_news_article
from ..models.news_article import NewsArticle
from ....Backend.db import news_articles_collection

router = APIRouter()

@router.get("/allnews/")
def get_tasks():
    return scrape_all()

@router.get("/dummy_news")
def get_dummy_news():
    return dummy_news()

@router.get("/news-article/{article_id}")
def get_single_news(article_id:int):
    return get_news_article(article_id)

@router.post("/news_article/", response_model=NewsArticle)
async def create_news_article(news_article: NewsArticle):
    # Insert the NewsArticle data into MongoDB (same code as before)
    inserted_article = await news_articles_collection.insert_one(news_article.dict())
    
    # Return the inserted article with the generated ObjectId
    return {**news_article.dict(), "id": str(inserted_article.inserted_id)}
