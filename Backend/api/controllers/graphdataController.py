from motor.motor_asyncio import AsyncIOMotorCollection
from ..database import db
from ..models.VehicleInfo import VehicleInfo
from ..models.TimeofDayInfo import TimeofDayInfo

model_name_mapping = {
    "vehicle_info": "VehicleInfo",
    "timeofday_info": "TimeofDayInfo",
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
            print("haha: ")
            print(count_to_add)
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

   