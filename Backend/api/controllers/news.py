import requests
from bs4 import BeautifulSoup
from ..database.db import news_articles_collection
from ..models.NewsArticle import NewsArticle


url1 = 'https://en.prothomalo.com/'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                    'AppleWebKit/537.11 (KHTML, like Gecko) '
                    'Chrome/23.0.1271.64 Safari/537.11',
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
    news = []
    cursor = news_articles_collection.find({})
    async for document in cursor:
        news.append(NewsArticle(**document))
    return news

async def create_news(news):
    document = news
    result = await news_articles_collection.insert_one(document)
    # document["ss"] = str(result.inserted_id)
    # print(document)
    return document
