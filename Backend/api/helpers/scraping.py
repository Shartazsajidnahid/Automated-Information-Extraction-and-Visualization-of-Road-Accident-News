import requests
from ..controllers.news import create_news
from ..models.NewsArticle import NewsArticle
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import csv
import os
from pytz import timezone

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
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome() 
    driver.maximize_window()
    driver.get(url)

    load_more_button = driver.find_element(By.CLASS_NAME, "more")

    time.sleep(1)
    actions = ActionChains(driver)
    all_news = []
    all_link = []
    confirm = driver.find_element(By.ID, "rcc-confirm-button")
    actions.click(confirm)
    actions.perform()
    stop = False
    # print("clicked")
    inserted = 0
    while load_more_button:
        print("Total : ", len(all_link))
        driver.execute_script("""
                             var element = document.querySelector(".bottom-container");
                            if (element)
                              element.parentNode.removeChild(element);
                              """)
        # confirmwindow = driver.find_element(By.ID, "gdpr-policy")
        # driver.execute_script("""
        # var element = arguments[0];
        # element.parentNode.removeChild(element);
        # """, element)
        
                            #   var element2 = document.querySelector("#");
                            # if (element2)
                            #   element2.parentNode.removeChild(element2);
        actions.click(load_more_button)
        actions.perform()
        print("Click action performed successfully")

        content = driver.find_elements(By.CLASS_NAME, "news_item")
        for item in content:
            a_tag = item.find_elements(By.TAG_NAME, 'a')
            href = a_tag[0].get_attribute("href")
            text = a_tag[0].get_attribute("text")
            title_tag = item.find_elements(By.TAG_NAME, 'span')
            title = title_tag[0].text
            if href not in all_link:
                all_link.append(href)
                print("yes")
                content, english_date, bangla_date = scrape_news(href)
                news_item = NewsArticle(
                    title=str(title),
                    link=str(href),
                    source="Prothom Alo",
                    content=str(content),
                    actual_timestamp = english_date,
                    bangla_timestamp = bangla_date
                )
                if (len(content)>=100) and (len(content)<=2000):
                    # print(content)
                    
                    response = await create_news(news_item)
                    if response[1] == "yes":
                        inserted = inserted+1
                        print("inserted: ", inserted)
                    else:
                        print("some error occurred")

        load_more_button = driver.find_element(By.CLASS_NAME, "more")
        # print(load_more_button)

        if(inserted>=300):
            break
    
    driver.quit()
    # news_articles = scrape_all()
    # totals = len(all_news)
    return all_news

# async def scrape_all():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get(url)

#     load_more_button = driver.find_element(By.CLASS_NAME, "more")

#     time.sleep(1)
#     actions = ActionChains(driver)
#     all_titles = set()  # Use a set to store unique news article titles
#     all_news = []
    
#     # CSV file setup
#     csv_filename = "scraped_data.csv"
#     csv_file_exists = os.path.exists(csv_filename)

#     with open(csv_filename, 'a', newline='', encoding='utf-8') as csvfile:
#         fieldnames = ['title', 'content', 'source', 'link']
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#         # Write header only if the file is newly created
#         if not csv_file_exists:
#             writer.writeheader()

#         while load_more_button:
#             print("all news: ", len(all_news))
#             time.sleep(10)
#             actions.click(load_more_button)
#             actions.perform()
#             content = driver.find_elements(By.CLASS_NAME, "news_item")
#             for item in content:
#                 a_tag = item.find_elements(By.TAG_NAME, 'a')
#                 href = a_tag[0].get_attribute("href")

#                 title_tag = item.find_elements(By.TAG_NAME, 'span')
#                 title = title_tag[0].text

#                 # Check if the news article title is already in the set
#                 if title not in all_titles:
#                     content = scrape_news(href)[0]

#                     news_item = NewsArticle(
#                         title=str(title),
#                         link=str(href),
#                         source="Prothom Alo",
#                         content=str(content)
#                     )

#                     if len(content) >= 100:
#                         all_news.append(news_item)
#                         all_titles.add(title)  # Add the title to the set

#                         # Write data to CSV
#                         writer.writerow({
#                             'title': news_item.title,
#                             'content': news_item.content,
#                             'source': news_item.source,
#                             'link': news_item.link
#                         })

#             load_more_button = driver.find_element(By.CLASS_NAME, "more")
#             if len(all_news) >= 1200:
#                 break

#     driver.quit()


def scrape_news(url):
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return "", ""

    soup = BeautifulSoup(response.text, 'html.parser')

    # Use a simple tag selector to find the <time> element
    time_element = soup.select_one('time')
    if time_element:
        english_date = time_element.get('datetime')
        bangla_date =  english_to_bangla_date(english_date)
    else:
        english_date = datetime.now()
        bangla_date = ""

    scraped_articles = []

    for news in soup.find_all('div', class_='story-element-text'):
        if news:
            content = news.text
            if content not in scraped_articles:
                scraped_articles.append(content)

    if not scraped_articles:
        return "", english_date, bangla_date

    full_story = " ".join(scraped_articles)

    return full_story, english_date, bangla_date



def english_to_bangla_date(english_date_str):
    english_date = datetime.strptime(english_date_str, "%Y-%m-%dT%H:%M:%S%z")
    bangladesh_timezone = timezone('Asia/Dhaka')
    english_date_in_bangladesh = english_date.astimezone(bangladesh_timezone)
    bangla_date = english_date_in_bangladesh.strftime("%d %B %Y, %I:%M %p")
    bangla_date = bangla_date.replace("0", "০").replace("1", "১").replace("2", "২").replace("3", "৩").replace("4", "৪").replace("5", "৫").replace("6", "৬").replace("7", "৭").replace("8", "৮").replace("9", "৯")
    return bangla_date


async def read_and_push_from_csv():
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the full path to the CSV file
    csv_filename = os.path.join(current_dir, "scraped_data.csv")    
    with open(csv_filename, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        inserted = 0
        totals = 0
        already = 0
        for row in reader:
            print(row['title'])
            if len(row['content'])>1500:
                continue
            totals = totals+1
            news_article = NewsArticle(
                title=row['title'],
                link=row['link'],
                source=row['source'],
                content=row['content']
            )

            response = await create_news(news_article)
            print(response)
            if response and response[1] == "yes":
                inserted += 1
                print("Inserted: ", inserted)
            elif response and response[1] == "no":
                already = already+1
                print("already: ", already)
        print("totals: ", totals)
        print("already in: ", already)

# Assuming you have a CSV file named "scraped_data.csv"
csv_filename = "scraped_data.csv"

