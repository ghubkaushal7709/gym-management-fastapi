from pydantic import BaseModel

class Member(BaseModel):
    name: str
    age: int
    plan: str

class Trainer(BaseModel):
    name: str
    specialty: str

class Plan(BaseModel):
    name: str
    price: int
    duration_days: int
