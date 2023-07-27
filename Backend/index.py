from fastapi import FastAPI
from api.routes import item, user

app = FastAPI()

app.include_router(item.router, prefix="/items", tags=["items"])
app.include_router(user.router, prefix="/users", tags=["users"])