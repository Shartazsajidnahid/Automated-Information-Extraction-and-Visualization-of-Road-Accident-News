from pydantic import BaseModel

class Parameter(BaseModel):
    location: str = "Example Location"
    time: str = "Example Time"
    vehicles: str = "Example Vehicles"
    dead: str = "Example Dead"
    injured: str = "Example Injured"

class NewsArticle(BaseModel):
    title: str
    content: str
    source: str
    link: str
    parameters: Parameter = Parameter()