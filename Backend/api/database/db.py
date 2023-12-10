from motor.motor_asyncio import AsyncIOMotorClient


MONGODB_URL = "mongodb://localhost:27017" 
DATABASE_NAME = "news"

# MongoDB client
client = AsyncIOMotorClient(MONGODB_URL)

# Database instance
db = client[DATABASE_NAME]
db2 = client["news2"]

# Collection for NewsArticles
news_articles_collection = db["news_articles"]

news_articles_collection2 = db2["news_articles"]

vehicle_info_collection = db["vehicle_info"]
timeofday_info_collection = db["timeofday_info"]
dayofweek_info_collection = db["dayofweek_info"]
district_info_collection = db["district_info"]
division_info_collecion = db["division_info"]


def get_collection(collection_name: str):
    return db[collection_name]
