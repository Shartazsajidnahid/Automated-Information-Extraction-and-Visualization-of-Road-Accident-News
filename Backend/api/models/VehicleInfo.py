from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
# from ...api.database.db import DATABASE_NAME

class VehicleInfo(BaseModel):

    typename: str
    occurrence: int = 0
    dead: int = 0
    injured: int = 0

# def initialize_vehicle_info_collection():
#     client = AsyncIOMotorClient("mongodb://localhost:27017")
#     db = client[DATABASE_NAME]

#     if "vehicle_info" not in db.list_collection_names():
#         vehicle_info_collection = db["vehicle_info"]
#         data = [
#             {"typename": "রবিবার"},
#             {"typename": "সোমবার"},
#             {"typename": "মঙ্গলবার"},
#             {"typename": "বুধবার"},
#             {"typename": "বৃহস্পতিবার"},
#             {"typename": "শুক্রবার"},
#             {"typename": "শনিবার"},
#         ]
#         vehicle_info_collection.insert_many(data)

