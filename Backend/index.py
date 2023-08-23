from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes import item, user

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Replace with your React app URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(item.router, prefix="/items", tags=["items"])
app.include_router(user.router, prefix="/users", tags=["users"])


