import os
import smtplib
import ssl
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)
now = datetime.now()
date_time = now.strftime("%d %B %Y")


@app.route("/")
@app.route("/home")
def home():
    recipes = list(
        [recipe for recipe in mongo.db.recipes.aggregate(
            [{"$sample": {"size": 9}}])])

    return render_template("home.html", recipes=recipes)


# Search 
@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        query = request.form.get("query")
        recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
        return render_template(
            "search_results.html", recipes=recipes)


# Register
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
        memorable_name = request.form.get("memorable-name")
        username = request.form.get("username")

        # check if password doesn't match confirm password
        if password != confirm_password:
            flash("Please ensure that your passwords match.")
            return redirect(url_for("register"))

        # check if memorable name matches username
        if memorable_name == username:
            flash("Please chose a unique Memorable Name")

        # check if memorable name matches password
        elif memorable_name == password:
            flash("Please chose a unique Memorable Name")
            return redirect(url_for("register"))

        # check if password and confirm password match
        if password == confirm_password:

            register = {
                "username": request.form.get("username").lower(),
                "password": generate_password_hash(
                    request.form.get("password").lower()),
                "upvotes": [],
                "memorable-name": generate_password_hash(
                    request.form.get("memorable-name").lower()),
                "email-address": request.form.get("email-address").lower()
                    }

        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Thank you for registering with Recipes Without.")
        return redirect(url_for("my_recipes", username=session["user"]))

    return render_template("register.html")


# Login
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
                existing_user["password"],
                    request.form.get("password")) and check_password_hash(
                existing_user["password"],
                    request.form.get("confirm-password")):
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


# Contact
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
            server.login(sender, password)
            server.sendmail(sender, receiver, message)

        flash("Your email has been sent")
    return render_template("contact.html")


# Send password reset link
# This section copied and adapted from
# https://realpython.com/lessons/sending-plaintext-emails-python/
@app.route("/send_password_reset", methods=["GET", "POST"])
def send_password_reset():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username1").lower()})
        email = mongo.db.users.find_one(
            {"email-address": request.form.get("email1")})
        if existing_user and email:
            smtp_server = "smtp.gmail.com"
            port = 465
            sender = "recipetest17@gmail.com"
            password = os.environ.get("PASSWORD")

            name = request.form["username1"]
            email = "recipetest17@gmail.com"

            receiver = request.form["email1"]

            message = f"""\
            From: "Recipes Without"

            Email from {email}
            Hello {name},
            Please Click the link to reset your password:
            https://recipes-without.herokuapp.com/reset_password
            """
            context = ssl.create_default_context()

            with smtplib.SMTP_SSL(
                    smtp_server, port, context=context) as server:

                server.login(sender, password)
                server.sendmail(sender, receiver, message)
            flash("Password reset link has been sent")
        else:
            flash("Incorrect Username or Password")
    return render_template("send_password_reset.html")


# Reset Password
@app.route("/reset_password", methods=["GET", "POST"])
def reset_password():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        new_password = {
            "password": generate_password_hash(
                    request.form.get("password").lower())
        }
        if existing_user:
            if check_password_hash(
                existing_user["memorable-name"],
                    request.form.get("memorable-name")):
                session["user"] = request.form.get("username").lower()
                mongo.db.users.update(
                    {"password": request.form.get(
                        "password").lower()}, new_password)
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

    return render_template("reset_password.html")


# Reset Password Form
@app.route("/reset_password_form", methods=["GET", "POST"])
def reset_password_form():
    if request.method == "POST":
        return render_template("reset_password")


# Manage Account
@app.route("/manage_account/<username>")
def manage_account(username):
    if "user" in session:
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]

        return render_template("manage_account.html", username=username)


# My Recipes
# code copied and adapted from 'Task Manager' mini project
@app.route("/my_recipes/<username>", methods=["GET", "POST"])
def my_recipes(username):
    if "user" in session:
        # get the session user's username from the db
        recipes = list(mongo.db.recipes.find({"added_by": username}))
        return render_template(
            "my_recipes.html", username=username,
            recipes=recipes)
    return redirect(url_for("login"))


# User Recipes
@app.route("/user_recipes/<username>", methods=["GET", "POST"])
def user_recipes(username):
    if "user" in session:
        # get the session user's username from the db
        recipes = list(mongo.db.recipes.find({"added_by": username}))
        return render_template(
            "user_recipes.html", username=username,
            recipes=recipes)
    return redirect(url_for("login"))


# Edit Recipe
# This section referenced and adapted from 'Tak Manager' walkthrough project.
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    if recipe['added_by'] == session.get("user", None):
        if request.method == "POST":
            edit = {
                    "category_name": request.form.get("category_name"),
                    "recipe_name": request.form.get("edit_recipe_name"),
                    "equipment_needed": request.form.get(
                        "edit_equipment_needed"),
                    "portions": request.form.get("edit_portions"),
                    "ingredients": request.form.get("edit_ingredients"),
                    "method": request.form.get("edit_method"),
                    "image": request.form.get("edit_image_url"),
                    "alt": request.form.get("edit_image_description"),
                    "added_by": session["user"],
                        }
            mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, edit)
            flash("Recipe Successfully Updated")

        recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
        categories = mongo.db.categories.find().sort("category_name", 1)
        return render_template(
            "edit_recipe.html",
            recipe=recipe, categories=categories)
    else:
        return redirect(url_for("home"))


# Delete Recipe
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    if recipe['added_by'] == session.get("user", None):
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
        flash("Recipe deleted!")
        return redirect(url_for("my_recipes", username=username))
    else:
        return redirect(url_for("home"))


# Delete User
@app.route("/delete_user/<username>")
def delete_user(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    if username == session["user"] or username == "admin":
        mongo.db.users.remove({"username": session["user"]})
        session.pop("user")
        flash("Your account has been deleted")
        return redirect(url_for(
            "register", username=username))
    else:
        return redirect(url_for("login"))


# Admin Section
@app.route("/admin/<username>")
def admin(username):
    username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
    recipe = list(mongo.db.recipes.find({"added_by": username}))
    if username == "admin":
        users = mongo.db.users.find()
        return render_template(
            "admin.html", username=username, users=users, recipe=recipe)


# Allow Admin to delete user account
@app.route("/admin_delete/<username>/<user_id>")
def admin_delete(username, user_id):
    username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
    if username == "admin":
        users = mongo.db.users.find({"_id": ObjectId(user_id)})
        for user in users:
            # mongo.db.users.remove({"_id": ObjectId(user_id)})
            mongo.db.users.delete_one(user)
            flash("User account has been deleted")
        return redirect(url_for("admin", username=username, users=users))


# Logout
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
    recipes = list(mongo.db.recipes.find(
        {"category_name": "Gluten Free"}))
    return render_template(
        "gluten_free.html", recipes=recipes)


# dairy free page
@app.route("/dairy_free")
def dairy_free():
    recipes = list(mongo.db.recipes.find(
        {"category_name": "Dairy Free"}
    ))
    return render_template("dairy_free.html", recipes=recipes)


# egg free page
@app.route("/egg_free")
def egg_free():
    recipes = list(mongo.db.recipes.find(
        {"category_name": "Egg Free"}))
    return render_template("egg_free.html", recipes=recipes)


# recipe page
@app.route("/recipe/<recipe_id>")
def recipe(recipe_id):
    recipes = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template(
        "recipe.html", recipes=recipes)


# Upvotes
# This code copied and adapted from an example posted on
# CI Slack by ShaneMuir_Alumni.
# Help was also received from Tim Nelson at Tutor Support
@app.route("/upvotes/<recipe_id>")
def upvotes(recipe_id):

    mongo.db.recipes.find_one_and_update(
        {"_id": ObjectId(recipe_id)},
        {"$inc": {"upvotes": 1}},
      )

    if "user" in session:
        mongo.db.users.find_one_and_update(
            {"username": session["user"]},
            {"$push": {"upvotes": ObjectId(recipe_id)}})

        mongo.db.users.find_one_and_update(
            {"username": session["user"]},
            {"$pull": {"downvotes": ObjectId(recipe_id)}})

        try:
            user_upvotes = mongo.db.users.find(
                {"username": session["user"]})["upvotes"]
        except:
            user_upvotes = []
        return redirect(url_for(
            "recipe", user_upvotes=user_upvotes, recipe_id=recipe_id))
    return redirect(url_for("recipe"))


# Downvotes
# This code copied and adapted from an example posted on
# CI Slack by ShaneMuir_Alumni.
# Help was also received from Tim Nelson at Tutor Support
@app.route("/downvotes/<recipe_id>")
def downvotes(recipe_id):
    mongo.db.recipes.find_one_and_update(
        {"_id": ObjectId(recipe_id)},
        {"$inc": {"downvotes": 1}}
        )

    if "user" in session:
        mongo.db.users.find_one_and_update(
            {"username": session["user"]},
            {"$push": {"downvotes": ObjectId(recipe_id)}})
        mongo.db.users.find_one_and_update(
            {"username": session["user"]},
            {"$pull": {"upvotes": ObjectId(recipe_id)}})
        try:
            user_downvotes = mongo.db.users.find(
                {"username": session["user"]})["downvotes"]
        except:
            user_downvotes = []
        return redirect(url_for(
            "recipe", user_downvotes=user_downvotes, recipe_id=recipe_id))
    return redirect(url_for("recipe"))


# Gluten Free Recipe
@app.route("/gluten_free_recipe/<recipe_id>")
def gluten_free_recipe(recipe_id):
    recipes = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template(
        "gluten_free_recipe.html", recipes=recipes)


# Dairy Free Recipe
@app.route("/dairy_free_recipe/<recipe_id>")
def dairy_free_recipe(recipe_id):
    recipes = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template(
        "dairy_free_recipe.html", recipes=recipes)


# Egg Free Recipe
@app.route("/egg_free_recipe/<recipe_id>")
def egg_free_recipe(recipe_id):
    recipes = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template(
        "egg_free_recipe.html", recipes=recipes)


# Add Recipes
# code copied and adapted from 'Task Manager' mini project
@app.route("/add_recipes", methods=["GET", "POST"])
def add_recipes():
    if request.method == "POST":
        recipe = {
            "category_name": request.form.get("category-name"),
            "recipe_name": request.form.get("recipe-name"),
            "equipment_needed": request.form.get("equipment-needed"),
            "portions": request.form.get("portions"),
            "ingredients": request.form.get("ingredients"),
            "method": request.form.get("method"),
            "added_by": session["user"],
            "image": request.form.get("image-url"),
            "added_on": date_time,
            "alt": request.form.get("image-description"),
            "upvotes": 0,
            "downvotes": 0
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Thank you for adding a new recipe!")
        return redirect(url_for("my_recipes", username=session["user"]))
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_recipes.html", categories=categories)


# Error handlers:
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def something_wrong(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
