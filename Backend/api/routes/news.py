from fastapi import APIRouter, HTTPException
from ..controllers.news import fetch_all_news, create_news, get_news_by_id
from ..controllers.dummynews import dummy_news, get_news_article
from ..models.NewsArticle import NewsArticle
from ..database.db import news_articles_collection
from bson import ObjectId 

router = APIRouter()

# @router.get("/allnews/")
# def get_tasks():
#     return scrape_all()

@router.get("/dummy_news")
def get_dummy_news():
    return dummy_news()


@router.get("/news-article/{article_id}")
async def get_single_news(article_id:str):
    return await get_news_by_id(article_id)


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