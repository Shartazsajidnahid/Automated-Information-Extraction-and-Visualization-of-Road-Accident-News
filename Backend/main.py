from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes.scrape import router as scrape
from api.routes.demo import router as demo

app = FastAPI()


# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Replace with your React app URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(scrape, prefix="/scrape")
app.include_router(demo, prefix="/demo")

