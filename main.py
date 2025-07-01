from database.db import create_tables
from fastapi import FastAPI,Depends, HTTPException
from routes.tasks import router as tasks_router
from sqlmodel import Session, select
from database.db import getsession  # Adjust to match your session function name
from models.models import Task

app=FastAPI()

app.include_router(tasks_router,prefix="/tasks")

@app.on_event("startup")
def build_tables():
    create_tables()

@app.get("/health", status_code=200)
def health_check(session: Session = Depends(getsession)):
    try:
        # Attempt a simple database query to verify connectivity
        session.execute(select(Task).limit(1))
        return {"status": "healthy", "message": "API and database are operational"}
    except Exception as e:
        raise HTTPException(status_code=503, detail="Service unavailable")


@app.get("/")
def index():
    endpoints = {
        "api_info": {
            "title": app.title,
            "description": app.title,
            "version": app.version,
            "health_check": "/tasks/health",
        },
        "available_endpoints": [
            {
                "method": "GET",
                "path": "/tasks/",
                "description": "List all tasks with optional filters (status, priority) and pagination"
            },
            {
                "method": "POST",
                "path": "/tasks/",
                "description": "Create a new task"
            },
            {
                "method": "GET",
                "path": "/tasks/{task_id}",
                "description": "Get a specific task by ID"
            },
            {
                "method": "PUT",
                "path": "/tasks/{task_id}",
                "description": "Update a specific task by ID"
            },
            {
                "method": "DELETE",
                "path": "/tasks/{task_id}",
                "description": "Delete a specific task by ID"
            },
            {
                "method": "GET",
                "path": "/tasks/status/{status}",
                "description": "Get tasks filtered by status"
            },
            {
                "method": "GET",
                "path": "/tasks/priority/{priority}",
                "description": "Get tasks filtered by priority"
            },
            {
                "method": "GET",
                "path": "/tasks/health",
                "description": "Check the API and database health status"
            }
        ]
    }
    return endpoints
