from fastapi import FastAPI
from todo import todo_router
app = FastAPI()

@app.get("/")
async def welcome():
    return {"message": "Hello FastAPI"}

app.include_router(todo_router)