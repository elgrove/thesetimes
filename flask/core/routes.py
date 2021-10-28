from flask import render_template
from core import app


@app.route("/")
def index():
    return render_template("home.html")


@app.route("/article")
def article():
    return render_template("article.html")
