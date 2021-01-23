import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/gluten_free")
def gluten_free():
    recipes = mongo.db.recipes.find()
    return render_template("gluten_free.html", recipes=recipes)


# code copied and adapted from 'Task Manager' mini project.
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if user is already registered and in database
        registered_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if registered_user:
            flash("Sorry, that username is already taken!")
            return redirect(url_for("register"))

        password = request.form.get("password")
        confirm_password = request.form.get("confirm-password")

        print(confirm_password)

        if password != confirm_password:
            flash("Please ensure that your passwords match.")
            return redirect(url_for("register"))

        if password == confirm_password:

            register = {
                "username": request.form.get("username").lower(),
                "password": generate_password_hash(
                    request.form.get("password").lower())
                    }

        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Thank you for registering with Recipes Without.")
        return redirect(url_for("my_recipes", username=session["user"]))

    return render_template("register.html")

# code copied from 'Task Manager' mini project
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "my_recipes", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# code copied from 'Task Manager' mini project
@app.route("/my_recipes/<username>", methods=["GET", "POST"])
def my_recipes(username):
    # get the session user's username from the db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("my_recipes.html", username=username)

    return redirect(url_for(login))


# code copied from 'Task Manager' mini project
@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have successfully logged out.")
    session.pop("user")
    return redirect(url_for("login"))


# recipe page
@app.route("/recipe")
def recipe():
    recipes = mongo.db.recipes.find()
    return render_template("recipe.html", recipes=recipes)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)