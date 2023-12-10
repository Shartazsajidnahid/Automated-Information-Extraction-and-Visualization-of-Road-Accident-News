from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
# from ...api.database.db import DATABASE_NAME

class DivisionInfo(BaseModel):

    typename: str
    occurrence: int = 0
    dead: int = 0
    injured: int = 0
