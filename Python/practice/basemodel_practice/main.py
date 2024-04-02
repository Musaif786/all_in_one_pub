from pydantic import BaseModel
from typing import List

class car(BaseModel):
    name: str
    number: int
    age: int
    subjects: List  = None


data ={
    "name": "Mohammed Musaif",
    "number": "955214575",
    "age": 25,
    "subjects": ["Englist","Maths","Science"]
}

obj = car(**data)
print(obj)
print(type(obj.number))
print(type(data["number"]))