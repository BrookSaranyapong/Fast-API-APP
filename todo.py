from fastapi import APIRouter, Path

todo_router = APIRouter()

todo_list = [
]
@todo_router.post("/todo")
async def add_todo(todo:dict):
    todo_list.append(todo)
    return {"message" : "To Add Successfully"}

@todo_router.get("/todo")
async def retrieve_todos():
    return {"todos": todo_list}