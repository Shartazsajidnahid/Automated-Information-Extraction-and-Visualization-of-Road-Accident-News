from pydantic import BaseModel
from datetime import datetime

class Parameter(BaseModel):
    location: str = "Example Location"
    division: str = "Division"
    district: str = "District"
    subdistrict: str = "Subdistrict"
    time: str = "Example Time"
    dayofweek: str = ""
    timeofday: str = ""
    vehicle1: str = ""
    vehicle2: str = ""
    dead: int = 0
    injured: int = 0

class NewsArticle(BaseModel):
    title: str
    content: str
    source: str
    link: str
    parameters: Parameter = Parameter()
    timestamp: datetime = datetime.now()
