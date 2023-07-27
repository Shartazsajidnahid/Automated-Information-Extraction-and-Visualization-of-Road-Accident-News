from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def read_items():
    return {"message": "Read all items"}
