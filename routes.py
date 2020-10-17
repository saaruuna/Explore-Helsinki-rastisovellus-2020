from app import app
from flask import redirect, render_template, request, session, make_response
from db import db
import users
import checkpoints
import performances

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
        user_id = users.user_id()
        username = users.username()
        return render_template("profile.html", username=username)
    if request.method == "POST":
        checkpoint_id = request.form["checkpoint_id"]
        checkpoint_name = checkpoints.get_checkpoint_name(checkpoint_id)
        file = request.files["file"]
        name = file.filename

        if not name.endswith(".jpg"):
            checkpointsList = checkpoints.get_checkpoints()
            return render_template("perform.html", message="Please submit a jpg!", checkpointsList=checkpointsList)

        data = file.read()

        if len(data) > 100*1024:
            checkpointsList = checkpoints.get_checkpoints()
            return render_template("perform.html", message="File size too large!", checkpointsList=checkpointsList)

        user_id = users.user_id()
        username = users.username()

        checkpoints.perform_checkpoint(data, user_id, checkpoint_id)
        return render_template("profile.html", username=username, message="You successfully performed your checkpoint!")

@app.route("/checkpoints")
def showCheckpoints():
    user_id = users.user_id()
    checkpointsList = checkpoints.get_checkpoints()
    return render_template("checkpoints.html", checkpointsList=checkpointsList)

@app.route("/perform")
def perform():
    checkpointsList = checkpoints.get_checkpoints()
    return render_template("perform.html", checkpointsList=checkpointsList)

@app.route("/gallery", methods=["GET","POST"])
def gallery():
    if request.method == "GET":
        user_id = users.user_id()
        performancesList = performances.get_performances(user_id)
        return render_template("gallery.html", performancesList=performancesList)

    if request.method == "POST":
        performance_id = request.form["performance"]
        return redirect("/gallery/" + str(performance_id))

@app.route("/gallery/<string:performance_id>")
def show(performance_id):
    if "username" in session:
        return performances.view_performance(performance_id)
    else:
        return render_template("login.html",message="Please log in to view your gallery!")
