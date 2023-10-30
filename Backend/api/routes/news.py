from fastapi import APIRouter, HTTPException
from ..controllers.news import fetch_all_news, create_news, get_news_by_id, fetch_latest_news
from ..controllers.dummynews import dummy_news, get_news_article
from ..models.NewsArticle import NewsArticle, Parameter
from ..database.db import news_articles_collection
from ..helpers.hugface import find_params
from ..helpers.bangla_transform import find_parameters
from ..helpers.find_district_location import locate
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

@router.get("/latest-news/")
async def get_latest_news():
    response = await fetch_latest_news()
    return response


@router.post("/news_article/")
async def create_news_article(news_article: NewsArticle):

    parameters = await find_parameters(news_article.content)
    if parameters:
        districts = locate(parameters["location"])
        new_params = Parameter(
            location=parameters["location"], 
            division = districts["division"],
            district = districts["district"],
            subdistrict = districts["subdistrict"],
            time = parameters["time"],
            vehicles = parameters["vehicle"],
            dead = parameters["dead"],
            injured = parameters["injured"]
             )
        # print(new_params)
        news_article.parameters = new_params
    # print(news_article) 
    
    response = await create_news(news_article)
    print({"response":response})
    if response:
        return "created successfully "
    raise HTTPException(400, "Something went wrong")