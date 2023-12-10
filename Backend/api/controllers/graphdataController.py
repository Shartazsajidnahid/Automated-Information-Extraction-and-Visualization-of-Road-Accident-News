from motor.motor_asyncio import AsyncIOMotorCollection
from ..database import db
from ..models.VehicleInfo import VehicleInfo
from ..models.TimeofDayInfo import TimeofDayInfo
from ..models.DistrictInfo import DistrictInfo
from ..models.DivisionInfo import DivisionInfo
from ..models.DayofWeekInfo import DayofWeekInfo
from ..models.NewsArticle import NewsArticle

model_name_mapping = {
    "vehicle_info": "VehicleInfo",
    "timeofday_info": "TimeofDayInfo",
    "district_info": "DistrictInfo",
    "division_info": "DivisionInfo",
    "dayofweek_info": "DayofWeekInfo"
}

async def update_occurrence(table_name: str, type_name: str, occurrence_type: str,  count_to_add: int):
    
    collection = db.get_collection(table_name)
    existing_data = await collection.find_one({"typename": type_name})

    if existing_data:
        updated_count = existing_data[occurrence_type] + count_to_add

        await collection.update_one(
            {"typename": type_name},
            {"$set": {occurrence_type: updated_count}}
        )
    else:
        model_name = model_name_mapping.get(table_name)

        if model_name:
            model_class = globals().get(model_name)
            if model_class:
                new_data = model_class(typename=type_name)
                setattr(new_data, occurrence_type, count_to_add)
                print(new_data)
                await collection.insert_one(new_data.dict())
            else:
                print(f"Model {model_name} not found.")
        else:
            print(f"Variable name {type_name} not found in the mapping.")


async def get_occurence_data(table_name: str, occurrence_type: str):
    collection: AsyncIOMotorCollection = db.get_collection(table_name)
    data_from_db = await collection.find({}).to_list(length=1000)

    # format the data based on occurrence_type
    transformed_data = [
        {"typename": item["typename"], "count": item[occurrence_type]}
         for item in data_from_db
    ]
    return transformed_data


async def updateGraphData(news_article: NewsArticle):
    division = news_article.parameters.division
    district = news_article.parameters.district
    vehicle1 = news_article.parameters.vehicle1
    vehicle2 = news_article.parameters.vehicle2
    tod = news_article.parameters.timeofday
    dow = news_article.parameters.dayofweek
    dead = news_article.parameters.dead
    injured = news_article.parameters.injured

    if len(division) >= 0:
        await update_one_table("division_info", division, dead, injured )
    if len(district) >= 0:
        await update_one_table("district_info", district, dead, injured )
    if len(vehicle1) >= 0:
        await update_one_table("vehicle_info", vehicle1, dead, injured )
    if len(vehicle2) >= 0:
        await update_one_table("vehicle_info", vehicle2, dead, injured )
    if len(tod) >= 0:
        await update_one_table("timeofday_info", tod, dead, injured )
    if len(dow) >= 0:
        await update_one_table("dayofweek_info", dow, dead, injured )     


async def update_one_table(table_name:str, typename: str, dead: int, injured: int):
    await update_occurrence(table_name, typename, "occurrence", 1)
    await update_occurrence(table_name, typename, "dead", dead)
    await update_occurrence(table_name, typename, "injured", injured)

# for entry in your_array:
#         district_name = entry["typename"]
#         occurrence_value = entry["occurrence"]
#         dead_value = entry["dead"]
#         injured_value = entry["injured"]

#         await update_occurrence("district_info", district_name, "occurrence", occurrence_value)
#         await update_occurrence("district_info", district_name, "dead", dead_value)
#         await update_occurrence("district_info", district_name, "injured", injured_value)
