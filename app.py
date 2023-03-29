from fastapi import FastAPI, APIRouter

app = FastAPI(host="0.0.0.0")

@app.get("/")
def root():
    return {"hello":"world"}

users = APIRouter(prefix="/users",)
@users.get("")
def get_users_all():
    return "users all"

@users.get("/me")
def get_users_me():
    return "users me"

app.include_router(users)