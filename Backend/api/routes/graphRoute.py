from fastapi import APIRouter
from ..controllers.graphdataController import get_occurence_data, highchartData
from fastapi.responses import JSONResponse
from .geolocations import bangladesh_district_geolocations

router = APIRouter()

def get_district_coordinates(district, intensity):
    if district in bangladesh_district_geolocations:
        coordinates = bangladesh_district_geolocations[district]
        return coordinates + [intensity*300]
    else:
        return None


@router.get("/get-data-by-type/")
async def get_data_by_type(table_name: str, occurrence_type: str):
    try:
        response = await get_occurence_data(table_name, occurrence_type)
        return response
        # return JSONResponse(content=respoxnse)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@router.get("/get-data/")
async def get_data(table_name: str):
    try:
        response = await get_occurence_data(table_name, "occurrence")
        return response
        # return JSONResponse(content=respoxnse)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@router.get("/get-heatmap-data/")
async def get_heatmap_data(occurrence_type: str):
    
    try:
        response = await get_data_by_type("district_info", occurrence_type)
        result_array = []
        for entry in response:
            district_name = entry["typename"]
            count_value = entry["count"]

            result = get_district_coordinates(district_name, count_value)

            if result is not None:
                result_array.append(result)
        # for item in result_array:
        #     print(item)
        return result_array
        # return JSONResponse(content=respoxnse)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@router.get("/get-highchart-data")
async def get_highchart_data():
    return await highchartData()

dummy_data = [
    {"lat": 23.8103, "lon": 90.4125, "value": 10},
    {"lat": 24.3636, "lon": 88.6241, "value": 5},
    {"lat": 23.6850, "lon": 90.3563, "value": 8},
    # Add more dummy data points as needed
]

@router.get("/getmapdata")
async def get_custom_data():
    return dummy_data
    