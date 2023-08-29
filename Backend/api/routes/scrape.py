from fastapi import APIRouter
from ..controllers.scrape import scrape_all

router = APIRouter()

@router.get("/news/")
def get_tasks():
    return scrape_all()



# @router.post("/news/")
# async def create_task(request: Request):
#     body = await request.body()
#     return {"message": "Task created successfully", "task": body} 
