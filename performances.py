from app import app
from db import db
from flask import redirect, render_template, request, session, flash, make_response

def get_performances(user_id):
    sql = "SELECT performances.performance_id, checkpoints.name, checkpoints.category FROM checkpoints INNER JOIN performances ON performances.checkpoint_id=checkpoints.checkpoint_id INNER JOIN users ON users.user_id=performances.user_id WHERE users.user_id=:user_id ORDER BY performances.performance_id"
    result = db.session.execute(sql, {"user_id":user_id})
    list = result.fetchall()
    return list

def view_performance(performance_id):
    sql = "SELECT data FROM performances WHERE performance_id=:performance_id"
    result = db.session.execute(sql, {"performance_id":performance_id})
    data = result.fetchone()[0]
    response = make_response(bytes(data))
    response.headers.set("Content-Type","image/jpeg")
    return response
