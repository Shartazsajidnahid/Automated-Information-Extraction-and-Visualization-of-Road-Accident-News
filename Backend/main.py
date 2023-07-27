from fastapi import FastAPI
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

tasks = ["first tast", "second task"]

@app.get("/tasks/")
def get_tasks():
    return tasks

@app.post("/tasks/")
def create_task(task: str):
    tasks.append(task)
    return {"message": "Task created successfully", "task": task}


#from maccc