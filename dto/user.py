# data to object (object definition)

from pydantic import BaseModel

class User(BaseModel):
    first_name: str
    middle_name: str
    last_name: str
    age: int
    height: int
    email: str