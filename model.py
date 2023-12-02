from pydantic import BaseModel
from typing import List

class Todo(BaseModel):
    id:int
    item: str

    class Config:
        json_schema_extra = {
            "example": {
                "id":1,
                "item": "What we doing today?"
            }
        }

class TodoItem(BaseModel):
    item: str
    class Config:
        json_schema_extra = {
            "example": {
                "item": "What we doing today?"
            }
        }

class TodoItems(BaseModel):
    todos: List[Todo]
    class Config:
        json_schema_extra = {
            "example": {
                "todos":[
                    {
                        "id":1,
                        "item": "What we doing today?"
                    },
                    {
                        "id":2,
                        "item": "Sleeping"
                    }
                ]
            }
        }