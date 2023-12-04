import requests
from ..controllers.news import create_news
from ..models.NewsArticle import NewsArticle
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
import csv
import os

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


# async def scrape_all():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get(url)

#     load_more_button = driver.find_element(By.CLASS_NAME, "more")

#     time.sleep(1)
#     actions = ActionChains(driver)
#     all_links= []
#     all_news = []
#     # print("clicked")
#     while load_more_button:
#         print("all news: ", len(all_news))
#         time.sleep(10)
#         actions.click(load_more_button)
#         actions.perform()
#         content = driver.find_elements(By.CLASS_NAME, "news_item")
#         for item in content:
#             a_tag = item.find_elements(By.TAG_NAME, 'a')
#             href = a_tag[0].get_attribute("href")
#             text = a_tag[0].get_attribute("text")
#             title_tag = item.find_elements(By.TAG_NAME, 'span')
#             title = title_tag[0].text
#             content = scrape_news(href)[0]
#             # print(content)

#             news_item = NewsArticle(
#                 title=str(title),
#                 link=str(href),
#                 source="Prothom Alo",
#                 content=str(content)
#             )
                
#             # all_links.append(href)
#             # print(news_item)
#             if(len(content)>=100):
#                 all_news.append(news_item)

#         load_more_button = driver.find_element(By.CLASS_NAME, "more")
#         if(len(all_news)>=1500):
#             break
#     driver.quit()
#     # news_articles = scrape_all()
#     totals = len(all_news)

#     inserted = 0
#     for news_article in all_news:
        
#         response = await create_news(news_article)
#         if response[2] == "yes":
#             inserted = inserted+1
#             print("inserted: ", inserted)
#     #     print("some error occurred")
#     return all_news

async def scrape_all():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)

    load_more_button = driver.find_element(By.CLASS_NAME, "more")

    time.sleep(1)
    actions = ActionChains(driver)
    all_titles = set()  # Use a set to store unique news article titles
    all_news = []
    
    # CSV file setup
    csv_filename = "scraped_data.csv"
    csv_file_exists = os.path.exists(csv_filename)

    with open(csv_filename, 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['title', 'content', 'source', 'link']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write header only if the file is newly created
        if not csv_file_exists:
            writer.writeheader()

        while load_more_button:
            print("all news: ", len(all_news))
            time.sleep(10)
            actions.click(load_more_button)
            actions.perform()
            content = driver.find_elements(By.CLASS_NAME, "news_item")
            for item in content:
                a_tag = item.find_elements(By.TAG_NAME, 'a')
                href = a_tag[0].get_attribute("href")

                title_tag = item.find_elements(By.TAG_NAME, 'span')
                title = title_tag[0].text

                # Check if the news article title is already in the set
                if title not in all_titles:
                    content = scrape_news(href)[0]

                    news_item = NewsArticle(
                        title=str(title),
                        link=str(href),
                        source="Prothom Alo",
                        content=str(content)
                    )

                    if len(content) >= 100:
                        all_news.append(news_item)
                        all_titles.add(title)  # Add the title to the set

                        # Write data to CSV
                        writer.writerow({
                            'title': news_item.title,
                            'content': news_item.content,
                            'source': news_item.source,
                            'link': news_item.link
                        })

            load_more_button = driver.find_element(By.CLASS_NAME, "more")
            if len(all_news) >= 1200:
                break

    driver.quit()


def convert_to_bangla(datetime_str):
    # Convert to datetime object
    dt_object = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S%z")

    # Define Bangla digits
    bangla_digits = ["০", "১", "২", "৩", "৪", "৫", "৬", "৭", "৮", "৯"]

    # Convert each digit in the timestamp to Bangla digit
    bangla_timestamp = "".join([bangla_digits[int(digit)] if digit.isdigit() else digit for digit in dt_object.strftime("%Y-%m-%d %H:%M:%S%z")])

    return bangla_timestamp

def scrape_news(url):
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return "", ""

    soup = BeautifulSoup(response.text, 'html.parser')

    scraped_articles = []

    for news in soup.find_all('div', class_='story-element-text'):
        if news:
            content = news.text
            if content not in scraped_articles:
                scraped_articles.append(content)

    if not scraped_articles:
        return "", ""

    full_story = " ".join(scraped_articles)

    # Extract timestamp
    timestamp_element = soup.find('time')
    timestamp = timestamp_element['datetime'] if timestamp_element else ""

    # Convert timestamp to Bangla
    bangla_timestamp = convert_to_bangla(timestamp)

    return full_story, timestamp, bangla_timestamp

# Example usage:
# url = "https://www.prothomalo.com/bangladesh/capital/7uwkl4mvut"
# content, timestamp, banglatimestamp = scrape_news(url)
# print("Content:", content)
# print("Timestamp:", timestamp)
# print("Timestamp (Bangla):", banglatimestamp)


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
            totals = totals+1
            news_article = NewsArticle(
                title=row['title'],
                link=row['link'],
                source=row['source'],
                content=row['content']
            )
            # print(news_article)

            response = await create_news(news_article)
            print(response)
            if response and response[2] == "yes":
                inserted += 1
                print("Inserted: ", inserted)
            elif response and response[2] == "no":
                already = already+1
                print("already: ", already)
        print("totals: ", totals)
        print("already in: ", already)

# Assuming you have a CSV file named "scraped_data.csv"
csv_filename = "scraped_data.csv"

