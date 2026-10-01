from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="TaskFlow API",
    version="0.1.0",
    description="A task management API built while learning FastAPI.",
)


# ---------- 1.3 Your first endpoint ----------
@app.get("/health")
def health_check():
    return {"status": "ok"}


# ---------- 1.6 Request body model ----------
# (This is a temporary mini-model. In Module 2 we replace it
#  with the proper TaskCreate / TaskRead / TaskUpdate in app/schemas/.)
class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    priority: str = "medium"


# ---------- 1.5 Query parameters ----------
@app.get("/tasks")
def list_tasks(
    skip: int = 0,
    limit: int = 10,
    completed: bool | None = None,
    search: str | None = None,
):
    return {"skip": skip, "limit": limit, "completed": completed, "search": search}


# ---------- 1.6 Request body endpoint ----------
@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    return {"id": 1, **task.model_dump()}


# ---------- 1.4 Path parameter ----------
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    return {"task_id": task_id, "title": "Buy milk"}