from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel
import pymysql

class User(BaseModel):
    email: str
    password: str

def connect():
    return pymysql.connect(
        host = "localhost",
        user="root",password="password",
        db="mydb"
    )

app = FastAPI()
users = APIRouter(prefix="/users")

@users.post("")
def create_user(user:User):
    conn = connect()
    conn.cursor().execute("insert into users(email,password) values (%s,%s)",
                (user.email,user.password))
    conn.commit()
    conn.close()
    return HTTPException(200,{"wow":"!"})
    
@users.get("")
def read_users():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("select * from users")
    rows = cursor.fetchall()
    conn.close()
    return HTTPException(200,{"users":rows})

@users.put("")
def update_user(email:str, user:User):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        # PUT /users?email=john@example.com
        "update users set email=%s, password=%s where email=%s",
        (user.email, user.password, email)
        # "update users set email=%s, password=%s where id=%s",
        # (user.email, user.password, user_id)
    )
    conn.commit()
    conn.close()
    return HTTPException(200,{"message":f"updated user {user.email}"})

@users.delete("/{user_id}")
def delete_user(user_id:int):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("delete from users where id=%s",(user_id,))
    conn.commit()
    conn.close()
    return HTTPException(200,{"message":f"deleted user {user_id}"})

app.include_router(users)