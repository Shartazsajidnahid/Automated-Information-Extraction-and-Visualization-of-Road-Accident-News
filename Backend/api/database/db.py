# app/db.py

from motor.motor_asyncio import AsyncIOMotorClient

MONGODB_URL = "mongodb://localhost:27017"  # Update with your MongoDB server URL
DATABASE_NAME = "news"

# MongoDB client
client = AsyncIOMotorClient(MONGODB_URL)

# Database instance
db = client[DATABASE_NAME]

# Collection for NewsArticles
news_articles_collection = db["news_articles"]
