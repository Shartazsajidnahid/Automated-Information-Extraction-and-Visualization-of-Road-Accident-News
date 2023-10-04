from fastapi import APIRouter
from ..controllers.scrape import scrape_all
from ..controllers.dummynews import dummy_news


router = APIRouter()

@router.get("/news/")
def get_tasks():
    return scrape_all()

@router.get("/dummy_news")
def get_dummy_news():
    return dummy_news()



# @router.post("/news/")
# async def create_task(request: Request):
#     body = await request.body()
#     return {"message": "Task created successfully", "task": body} 
