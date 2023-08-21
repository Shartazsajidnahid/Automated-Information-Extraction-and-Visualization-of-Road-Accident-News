from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import requests
from bs4 import BeautifulSoup
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

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Replace with your React app URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

tasks = ["first task", "second task", "hahaha", "no country"]

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
            item = {"content": content, "link": link}
            if(content not in scraped_articles):
                scraped_articles.append(item)


@app.get("/news/")
def get_tasks():
    return scraped_articles

@app.post("/news/")
async def create_task(request: Request):
    body = await request.body()
    return {"message": "Task created successfully", "task": body} 


