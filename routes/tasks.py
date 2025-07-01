from fastapi import APIRouter,Depends,HTTPException
from schemas.task import TaskCreate,TaskResponse,TaskUpdate
from database.db import getsession
from sqlmodel import Session,select
from models.models import Task
from datetime import datetime,timezone
from typing import Optional
from enums import TaskStatus,TaskPriority
router=APIRouter()


@router.post("/",response_model=TaskResponse,status_code=201)
def create_task(task:TaskCreate,session:Session=Depends(getsession)):
    db_task = Task(**task.model_dump())
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task

@router.get("/{task_id}",response_model=TaskResponse,status_code=200)
def get_task_byId(task_id:int,session:Session=Depends(getsession)):
    db_task=session.get(Task,task_id)
    if not db_task:
        raise HTTPException(404,"There's no task with this id")
    return db_task

@router.put("/{task_id}",response_model=TaskResponse)
def update_task(task_id:int ,taskUpdated:TaskUpdate ,session:Session=Depends(getsession)):
    db_task=session.get(Task,task_id)
    if not db_task:
        raise HTTPException(404,"There's no task with this id")
    update_data = taskUpdated.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_task, key, value)
    db_task.updated_at = datetime.now(timezone.utc).replace(tzinfo=None)
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task

@router.delete("/{task_id}",status_code=204)
def delete_task(task_id:int ,taskUpdated:TaskUpdate ,session:Session=Depends(getsession)):
    db_task=session.get(Task,task_id)
    if not db_task:
        raise HTTPException(404,"There's no task with this id")
    session.delete(db_task)
    session.commit()
    return {"message":"task was deleted successfuly"}

@router.get("/",response_model=list[TaskResponse])
def get_tasks(skip:int=0 , 
              limit:int=10,
              status:Optional[TaskStatus]=None,
              priority:Optional[TaskPriority]=None
              ,session:Session=Depends(getsession)):
    query=select(Task)
    if status:
        query=query.where(status==Task.status)
    if priority:
        query=query.where(priority==Task.priority)
    tasks=session.execute(query.offset(skip).limit(limit))
    tasks = tasks.scalars().all()
    return tasks
@router.get("/status/{status}",response_model=list[TaskResponse])
def get_tasks_by_status(status:TaskStatus,session:Session=Depends(getsession)):
    query=select(Task).where(status==Task.status)
    result = session.execute(query)
    tasks = result.scalars().all()
    if not tasks:
        raise HTTPException(status_code=404, detail=f"No tasks found with status: {status}")
    return tasks
@router.get("/priority/{priority}",response_model=list[TaskResponse])
def get_tasks_by_status(priority:TaskPriority,session:Session=Depends(getsession)):
    query=select(Task).where(priority==Task.priority)
    result = session.execute(query)
    tasks = result.scalars().all()
    if not tasks:
        raise HTTPException(status_code=404, detail=f"No tasks found with status: {priority}")
    return tasks
