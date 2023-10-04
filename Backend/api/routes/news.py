from fastapi import APIRouter
from ..controllers.news import scrape_all
from ..controllers.dummynews import dummy_news, get_news_article


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



# @router.post("/news/")
# async def create_task(request: Request):
#     body = await request.body()
#     return {"message": "Task created successfully", "task": body} 

