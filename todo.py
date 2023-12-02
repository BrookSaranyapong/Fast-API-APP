from fastapi import APIRouter, Path, HTTPException, status
from model   import Todo, TodoItem

todo_router = APIRouter(tags=["Todo"])

todo_list = []

@todo_router.post("/todo")
async def add_todo(todo:Todo):
    for todo_data in todo_list:
        if todo_data.id == todo.id:
            return {"message" : "Todo with ID exist!"}
    todo_list.append(todo)
    return {"message" : "To Add Successfully"}

@todo_router.get("/todo")
async def retrieve_todos():
    return {"todos": todo_list}

@todo_router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int = Path(..., title="The ID of todo")):
    for todo in todo_list:
        if todo.id == todo_id:
            return {"todo" : todo}
    # return {"message": "Todo with ID doesn't exist!"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with ID doesn't exist!"
    )

@todo_router.put("/todo/{todo_id}")
async def update_todo(todo_data:TodoItem,todo_id: int):
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {"message": "Todo updated successfully"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with ID doesn't exist!"
    )

@todo_router.delete("/todo/{todo_id}")
async def delete_todo(todo_id: int):
    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo.id == todo_id:
            todo_list.pop(index)
            return {"message": "Todo deleted successfully"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with ID doesn't exist!"
    )

@todo_router.delete("/todo")
async def delete_all_todo():
    todo_list.clear()
    return {"message": "Todo deleted successfully"}
