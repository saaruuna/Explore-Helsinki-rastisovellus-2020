from app import app
from db import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask import redirect, render_template, request, session, flash

def login(username,password):
    sql = "SELECT password, user_id FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if user == None:
        return False
    else:
        if check_password_hash(user[0],password):
            session["user_id"] = user[1]
            return True
        else:
            return False

def user_id():
    return session.get("user_id",0)

def logout():
    del session["user_id"]

def register(username,password):
    hash_value = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (username,password) VALUES (:username,:password)"
        db.session.execute(sql, {"username":username,"password":hash_value})
        db.session.commit()
    except:
        return False
    return login(username,password)

def username():
    user_id = session.get("user_id",0)
    sql = "SELECT username FROM users WHERE user_id=:user_id"
    result = db.session.execute(sql, {"user_id":user_id})
    username = result.fetchone()[0]
    return username
