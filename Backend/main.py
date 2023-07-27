from fastapi import FastAPI

app = FastAPI()

tasks = ["first tast", "second task"]

@app.get("/tasks/")
def get_tasks():
    return tasks

@app.post("/tasks/")
def create_task(task: str):
    tasks.append(task)
    return {"message": "Task created successfully", "task": task}
