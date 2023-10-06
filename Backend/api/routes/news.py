from fastapi import APIRouter, HTTPException
from ..controllers.news import scrape_all, fetch_all_news, create_news
from ..controllers.dummynews import dummy_news, get_news_article
from ..models.NewsArticle import NewsArticle
from ..database.db import news_articles_collection

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


@router.get("/news-article/")
async def get_allnews():
    response = await fetch_all_news()
    return response

@router.post("/news_article/", response_model=NewsArticle)
async def create_news_article(news_article: NewsArticle):
    response = await create_news(news_article.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong")