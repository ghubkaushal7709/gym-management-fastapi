
from fastapi import FastAPI
from schemas import Member, Trainer, Plan
import crud

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Gym API Running"}

# MEMBER APIs
@app.post("/members")
def create_member(member: Member):
    return crud.add_member(member)

@app.get("/members")
def all_members():
    return crud.get_members()

@app.get("/members/{member_id}")
def one_member(member_id: int):
    return crud.get_member(member_id)

@app.delete("/members/{member_id}")
def remove_member(member_id: int):
    return crud.delete_member(member_id)

# TRAINER APIs
@app.post("/trainers")
def create_trainer(trainer: Trainer):
    return crud.add_trainer(trainer)

@app.get("/trainers")
def all_trainers():
    return crud.get_trainers()

# PLAN APIs
@app.post("/plans")
def create_plan(plan: Plan):
    return crud.add_plan(plan)

@app.get("/plans")
def all_plans():
    return crud.get_plans()

# SEARCH + PAGINATION
@app.get("/search")
def search(name: str):
    return crud.search_members(name)

@app.get("/paginate")
def paginate(skip: int = 0, limit: int = 2):
    return crud.paginate_members(skip, limit)

# WORKFLOW APIs
@app.post("/register")
def register(member: Member):
    new_member = crud.add_member(member)
    return {"message": "Registered", "member": new_member}

@app.post("/payment/{member_id}")
def payment(member_id: int):
    member = crud.get_member(member_id)
    if member:
        member["payment_status"] = "Paid"
        member["status"] = "Active"
        return {"message": "Payment successful", "member": member}
    return {"message": "Member not found"}

# DASHBOARD
@app.get("/dashboard")
def dashboard():
    return {
        "total_members": len(crud.members),
        "total_trainers": len(crud.trainers),
        "total_plans": len(crud.plans)
    }
