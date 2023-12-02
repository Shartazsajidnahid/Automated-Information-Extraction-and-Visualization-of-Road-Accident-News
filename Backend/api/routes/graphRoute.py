from fastapi import APIRouter
from ..controllers.graphdataController import get_occurence_data
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/get-data/{table_name}/{occurrence_type}")
async def get_data(table_name: str, occurrence_type: str):
    try:
        response = await get_occurence_data(table_name, occurrence_type)
        print(response)
        return response
        # return JSONResponse(content=respoxnse)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


dummy_data = [
    {"lat": 23.8103, "lon": 90.4125, "value": 10},
    {"lat": 24.3636, "lon": 88.6241, "value": 5},
    {"lat": 23.6850, "lon": 90.3563, "value": 8},
    # Add more dummy data points as needed
]

@router.get("/getmapdata")
async def get_custom_data():
    return dummy_data
    