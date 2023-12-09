import requests
from fastapi import HTTPException
from bs4 import BeautifulSoup
from ..database.db import news_articles_collection, news_articles_collection2
from ..models.NewsArticle import NewsArticle, Parameter
from bson import ObjectId 
from ..helpers.bangla_transform import find_parameters
from ..helpers.find_district_location import locate
from ..helpers import process_news_tokens
from datetime import datetime
from ..controllers.graphdataController import update_occurrence

url1 = 'https://en.prothomalo.com/'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                    'AppleWebKit/537.11 (KHTML, like Gecko) '
                    'Chrome/23.0.1271.64 Safari/537 .11',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                    'Accept-Encoding': 'none',
                    'Accept-Language': 'en-US,en;q=0.8',
                    'Connection': 'keep-alive'
    }


def scrape_all():
    response = requests.get(url1, headers, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    # articles = soup.find_all('div')

    scraped_articles = []
    classname = ["news_item", "news_with_no_image", "numbered-story-headline-wrapper"]

    for cls in classname: 
        for news in soup.find_all('div', class_=cls):
            if(news):
                content = news.a.text
                link = news.a.get("href")
                headline = news.a.get("aria-label")
                item = {"content": content, "link": link, "headline": headline}
                if(content not in scraped_articles):
                    scraped_articles.append(item)
    
    return scraped_articles


async def fetch_all_news(): 
    # await update_occurrence("district_info", "জামালপুর", "occurrence", 12)
    
    news = []
    cursor = news_articles_collection2.find({}).sort("timestamp", -1)
    async for document in cursor:
        document['_id'] = str(document['_id'])
        news.append(document)
    return news

async def fetch_latest_news(): 
    news = []
    cursor = news_articles_collection.find({}).sort("timestamp", -1).limit(5)
    async for document in cursor:
        document['_id'] = str(document['_id'])
        news.append(document)
    return news



async def get_news_by_id(news_id: str):
    try:
        news_object_id = ObjectId(news_id)
        news_item = await news_articles_collection.find_one({"_id": news_object_id})
        if news_item:
            news_item["_id"] = str(news_item["_id"])
            # print(news_item)
            return news_item
        else:
            raise HTTPException(status_code=404, detail="News not found")
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid ObjectId format")


async def create_news(news_article: NewsArticle):
    parameters = await find_parameters(news_article.content)

    if parameters:
        districts = locate(parameters["location"])
        vehicle1, vehicle2, dow, tod, newtime = process_news_tokens.process_news(news_article.content, parameters["time"])
        
        new_params = Parameter(
            location=parameters["location"], 
            division = districts["division"],
            district = districts["district"],
            subdistrict = districts["subdistrict"],
            time = newtime,
            dayofweek = dow,
            timeofday = tod,
            vehicle1 = vehicle1,
            vehicle2 = vehicle2,
            dead = parameters["dead"],
            injured = parameters["injured"]
             )
        # print(new_params)
        # print(vehicles)
        news_article.parameters = new_params
    
    # print(news_article) 
    
    news_article.timestamp=datetime.now();
    # result = await news_articles_collection.insert_one(news_article.dict())
    # print(news_article)
    return news_article

async def create_news2(news_article: NewsArticle):
     # Check if the news article already exists in db
    existing_article = await news_articles_collection.find_one({"title": news_article.title})
    # existing_article2 = await news_articles_collection2.find_one({"title": news_article.title})

    # print(existing_article2)

    
    if existing_article is None:
        # If not in db, insert into  db2
        parameters = await find_parameters(news_article.content)

        if parameters:
            districts = locate(parameters["location"])
            vehicle1, vehicle2, dow, tod = process_news_tokens.process_news(news_article.content, parameters["time"])
            
            new_params = Parameter(
                location=parameters["location"], 
                division=districts["division"],
                district=districts["district"],
                subdistrict=districts["subdistrict"],
                time=parameters["time"],
                dayofweek=dow,
                timeofday=tod,
                vehicle1=vehicle1,
                vehicle2=vehicle2,
                dead=parameters["dead"],
                injured=parameters["injured"]
            )
            
            news_article.parameters = new_params
        news_article.timestamp = datetime.now()

        result_db = await news_articles_collection.insert_one(news_article.dict())
        result_db2 = await news_articles_collection2.insert_one(news_article.dict())
        
        return result_db2, news_article, "yes"
    else:
        # If already in db, do not insert into db2
        return None, None, "no"

    
    
   