from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Replace with your React app URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

tasks = ["first task", "second task"]

@app.get("/tasks/")
def get_tasks():
    return tasks

@app.post("/tasks/")
async def create_task(request: Request):
    body = await request.body()
    return {"message": "Task created successfully", "task": body} 


#from maccc