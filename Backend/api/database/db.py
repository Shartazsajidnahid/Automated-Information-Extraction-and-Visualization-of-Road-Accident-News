from motor.motor_asyncio import AsyncIOMotorClient


MONGODB_URL = "mongodb://localhost:27017" 
DATABASE_NAME = "news"

# MongoDB client
client = AsyncIOMotorClient(MONGODB_URL)

# Database instance
db = client[DATABASE_NAME]

# Collection for NewsArticles
news_articles_collection = db["news_articles"]
vehicle_info_collection = db["vehicle_info"]
timeofday_info_collection = db["timeofday_info"]


def get_collection(collection_name: str):
    return db[collection_name]
