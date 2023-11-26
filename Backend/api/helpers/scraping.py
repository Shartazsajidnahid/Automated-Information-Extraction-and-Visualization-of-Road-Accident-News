import requests
from ..controllers.news import create_news
from ..models.NewsArticle import NewsArticle
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


url = 'https://prothomalo.com/topic/সড়ক-দুর্ঘটনা'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                    'AppleWebKit/537.11 (KHTML, like Gecko) '
                    'Chrome/23.0.1271.64 Safari/537 .11',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                    'Accept-Encoding': 'none',
                    'Accept-Language': 'en-US,en;q=0.8',
                    'Connection': 'keep-alive'
    }


async def scrape_all():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)

    load_more_button = driver.find_element(By.CLASS_NAME, "more")

    time.sleep(1)
    actions = ActionChains(driver)
    all_links= []
    all_news = []
    # print("clicked")
    while load_more_button:
        time.sleep(10)
        actions.click(load_more_button)
        actions.perform()
        content = driver.find_elements(By.CLASS_NAME, "news_item")
        for item in content:
            a_tag = item.find_elements(By.TAG_NAME, 'a')
            href = a_tag[0].get_attribute("href")
            text = a_tag[0].get_attribute("text")
            title_tag = item.find_elements(By.TAG_NAME, 'span')
            title = title_tag[0].text
            content = scrape_news(href)
            # print(content)

            news_item = NewsArticle(
                title=str(title),
                link=str(href),
                source="Prothom Alo",
                content=str(content)
            )
                
            # all_links.append(href)
            # print(news_item)
            if(len(content)>=100):
                all_news.append(news_item)

        load_more_button = driver.find_element(By.CLASS_NAME, "more")
        if(len(all_news)>=600):
            break
    driver.quit()
    # news_articles = scrape_all()
    for news_article in all_news:
        response = await create_news(news_article)
        print(response)
    # print({"response":response})
    # if response:
    #     print("successful")
    #     return "created successfully "
    # else: 
    #     print("some error occurred")

    return all_news

def scrape_news(url): 
    response = requests.get(url, headers, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    # articles = soup.find_all('div')

    scraped_articles = []

    for news in soup.find_all('div', class_='story-element-text'):
        if(news):
            content = news.text
            # print(content)
            if(content not in scraped_articles):
                scraped_articles.append(content)

    full_story = ""
    for x in scraped_articles:
        full_story += x + " "
    return full_story