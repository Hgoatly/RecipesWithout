import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env
from datetime import datetime
import smtplib, ssl

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)
now = datetime.now()
date_time = now.strftime("%d %B %Y")


# This section copied and adapted from https://realpython.com/lessons/sending-plaintext-emails-python/
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        smtp_server = "smtp.gmail.com"
        port = 465
        sender = "recipetest17@gmail.com"
        password = os.environ.get("PASSWORD")

        name = request.form["name"]
        email = request.form["email"]

        receiver = "recipetest579@gmail.com"

        message = f"""\
        From: "{name}"

        Email from {email}
        {request.form['message']}
        """

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            print(f"sender is: {sender};")
            print(f"receiver is: {receiver};")
            print(f"statement is: {message};")

            server.login(sender, password)
            server.sendmail(sender, receiver, message)

    return render_template("contact.html")


@app.route("/")
@app.route("/home")
def home():
    recipes = list(
        [recipe for recipe in mongo.db.recipes.aggregate(
            [{"$sample": {"size": 9}}])])
    return render_template("home.html", recipes=recipes)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("search_results.html", recipes=recipes)


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


# code copied and adapted from 'Task Manager' mini project
@app.route("/my_recipes/<username>", methods=["GET", "POST"])
def my_recipes(username):
    if "user" in session:
        # get the session user's username from the db
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        recipes = list(mongo.db.recipes.find({"added_by": username}))
        return render_template(
            "my_recipes.html", username=username,
            recipes=recipes)
    return redirect(url_for("login"))


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        edit = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "equipment_needed": request.form.get("equipment_needed"),
            "portions": request.form.get("portions"),
            "ingredients": request.form.get("ingredients"),
            "method": request.form.get("method"),
            "image": request.form.get("image_url"),
            "added_by": session["user"],
            }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, edit)
        flash("Your recipe has been edited.")

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_recipe.html", recipe=recipe, categories=categories)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe deleted!")
    return redirect(url_for("my_recipes", username=username))


# code copied from 'Task Manager' mini project
@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have successfully logged out.")
    session.pop("user")
    return redirect(url_for("login"))


# gluten free page
@app.route("/gluten_free")
def gluten_free():
    recipes = mongo.db.recipes.find(
        {"category_name": "gluten_free"})
    return render_template(
        "gluten_free.html", recipes=recipes)


# dairy free page
@app.route("/dairy_free")
def dairy_free():
    recipes = list(mongo.db.recipes.find(
        {"category_name": "dairy_free"}
    ))
    return render_template("dairy_free.html", recipes=recipes)


# egg free page
@app.route("/egg_free")
def egg_free():
    recipes = mongo.db.recipes.find(
        {"category_name": "egg_free"})
    return render_template("egg_free.html", recipes=recipes)


# recipe page
@app.route("/recipe/<recipe_id>")
def recipe(recipe_id):
    recipes = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template(
        "recipe.html", recipes=recipes)


@app.route("/gluten_free_recipe/<recipe_id>")
def gluten_free_recipe(recipe_id):
    recipes = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template(
        "gluten_free_recipe.html", recipes=recipes)


@app.route("/dairy_free_recipe/<recipe_id>")
def dairy_free_recipe(recipe_id):
    recipes = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template(
        "dairy_free_recipe.html", recipes=recipes)


@app.route("/egg_free_recipe/<recipe_id>")
def egg_free_recipe(recipe_id):
    recipes = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template(
        "egg_free_recipe.html", recipes=recipes)


# code copied and adapted from 'Task Manager' mini project
@app.route("/add_recipes", methods=["GET", "POST"])
def add_recipes():
    if request.method == "POST":
        recipe = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "equipment_needed": request.form.get("equipment_needed"),
            "portions": request.form.get("portions"),
            "ingredients": request.form.get("ingredients"),
            "method": request.form.get("method"),
            "added_by": session["user"],
            "image": request.form.get("image_url"),
            "added_on": date_time,
            "alt": request.form.get("image_description")
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Thank you for adding a new recipe!")
        return redirect(url_for("my_recipes", username=session["user"]))
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_recipes.html", categories=categories)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)