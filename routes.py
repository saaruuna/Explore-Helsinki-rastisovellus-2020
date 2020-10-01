from app import app
from flask import redirect, render_template, request, session, flash
from db import db
from werkzeug.utils import secure_filename
from flask_wtf.file import FileField, FileAllowed, FileRequired
import users
import checkpoints

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username,password):
            return redirect("/profile")
        else:
            return render_template("login.html",message="Incorrect username or password!")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.register(username,password):
            return redirect("/")
        else:
            return render_template("register.html",message="Unable to create an account!")

@app.route("/profile", methods=["GET","POST"])
def profile():
    if request.method == "GET":
        return render_template("profile.html")
    if request.method == "POST":
        checkpoint = request.form["checkpoint"]
        return render_template("profile.html", message="You successfully performed " + checkpoint "!")

@app.route("/checkpoints")
def showCheckpoints():
    user_id = users.user_id()
    checkpointsList = checkpoints.get_checkpoints()
    return render_template("checkpoints.html", checkpointsList=checkpointsList)

@app.route("/perform")
def perform():
    checkpointNames = checkpoints.get_names()
    user_id = users.user_id()

    return render_template("perform.html", checkpointNames=checkpointNames)


@app.route("/gallery")
def gallery():
    return render_template("gallery.html")
