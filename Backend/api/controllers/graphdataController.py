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


async def highchartData():
    demo_data = [
        ['bd-da', 0], ['bd-kh', 0], ['bd-ba', 0],
        ['bd-cg', 0], ['bd-sy', 0], ['bd-rj', 0], ['bd-rp', 0], ['bd-my', 0]
    ]

    divisiondata = await get_occurence_data("division_info", "occurrence")
    
    # for item in divisiondata:
    #     print(item)

    for item in divisiondata:    #ময়মনসিংহ   
        if item.get('typename') == "ঢাকা": 
            demo_data[0][1] = item.get('count')
        elif item.get('typename') == "খুলনা": 
            demo_data[1][1] = item.get('count')
        elif item.get('typename') == "বরিশাল": 
            demo_data[2][1] = item.get('count')
        elif item.get('typename') == "চট্টগ্রাম": 
            demo_data[3][1] = item.get('count')
        elif item.get('typename') == "সিলেট": 
            demo_data[4][1] = item.get('count')
        elif item.get('typename') == "রাজশাহী": 
            demo_data[5][1] = item.get('count')
        elif item.get('typename') == "রংপুর": 
            demo_data[6][1] = item.get('count')
        elif item.get('typename') == "ময়মনসিংহ": 
            demo_data[0][1] += item.get('count')
            
    
    return demo_data



    