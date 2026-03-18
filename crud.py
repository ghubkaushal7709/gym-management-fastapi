
members = []
trainers = []
plans = []

# MEMBER CRUD
def add_member(member):
    member_id = len(members) + 1
    new_member = {
        "id": member_id,
        **member.dict(),
        "payment_status": "Pending",
        "status": "Inactive"
    }
    members.append(new_member)
    return new_member

def get_members():
    return members

def get_member(member_id):
    for m in members:
        if m["id"] == member_id:
            return m
    return None

def delete_member(member_id):
    for m in members:
        if m["id"] == member_id:
            members.remove(m)
            return {"message": "Deleted"}
    return {"message": "Not Found"}

# TRAINER CRUD
def add_trainer(trainer):
    trainer_id = len(trainers) + 1
    new_trainer = {"id": trainer_id, **trainer.dict()}
    trainers.append(new_trainer)
    return new_trainer

def get_trainers():
    return trainers

# PLAN CRUD
def add_plan(plan):
    plan_id = len(plans) + 1
    new_plan = {"id": plan_id, **plan.dict()}
    plans.append(new_plan)
    return new_plan

def get_plans():
    return plans

# SEARCH
def search_members(name):
    return [m for m in members if name.lower() in m["name"].lower()]

# PAGINATION
def paginate_members(skip, limit):
    return members[skip: skip + limit]
