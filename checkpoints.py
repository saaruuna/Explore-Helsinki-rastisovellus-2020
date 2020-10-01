from app import app
from db import db
from flask import redirect, render_template, request, session, flash


def get_checkpoints():
    sql = "SELECT name, category, description FROM checkpoints"
    result = db.session.execute(sql)
    list = result.fetchall()
    return list

def get_names():
    sql = "SELECT name FROM checkpoints"
    result = db.session.execute(sql)
    list = result.fetchall()
    return list

def get_checkpoint_id(name):
    sql = "SELECT checkpoint_id from checkpoint WHERE name=:name"
    result = db.session.execute(sql)
    return result

def perform_checkpoint(data, user_id, checkpoint_id):
    sql = "INSERT INTO performances (data, user_id, checkpoint_id) VALUES (:data,:user_id,:checkpoint_id)"
    db.session.execute(sql, {"data":data,"user_id":user_id,"checkpoint_id":checkpoint_id})
    db.session.commit()
