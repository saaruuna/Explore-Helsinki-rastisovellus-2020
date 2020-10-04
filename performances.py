from app import app
from db import db
from flask import redirect, render_template, request, session, flash

def get_performances(user_id):
    sql = "SELECT performances.performance_id, checkpoints.name, checkpoints.category FROM checkpoints INNER JOIN performances ON performances.checkpoint_id=checkpoints.checkpoint_id INNER JOIN users ON users.user_id=performances.user_id WHERE users.user_id=:user_id ORDER BY performances.performance_id"
    result = db.session.execute(sql, {"user_id":user_id})
    list = result.fetchall()
    return list
