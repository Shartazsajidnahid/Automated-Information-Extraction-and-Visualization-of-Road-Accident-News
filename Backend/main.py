from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes.news import router as news
from api.routes.demo import router as demo
from api.routes.sheets import router as sheets

app = FastAPI()


# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Replace with your React app URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(news, prefix="/news")
app.include_router(demo, prefix="/demo")
app.include_router(sheets, prefix="/exportsheet")

