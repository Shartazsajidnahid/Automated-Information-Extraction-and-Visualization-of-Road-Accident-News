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
    
    