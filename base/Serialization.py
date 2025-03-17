# Pydantic for Serialization and Deserialization


from pydantic import BaseModel
from typing import List

class User(BaseModel):
    id: int
    name: str
    is_active: bool
    roles: List[str]


user1 = {
    "id":1,
    "name": "Alibek",
    "is_active": True,
    "roles": ["admin", "editor"]
}


user = User(**user1)
print(user.model_dump())