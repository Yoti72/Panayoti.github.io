from flask import Blueprint, render_template

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/contact")
def contact():
    return render_template("contact.html")

@views.route("/projects")
def projects():
    return render_template("projects.html")