from flask import Blueprint, render_template

core = Blueprint("core", __name__, template_folder="templates")


@core.route("/", defaults={"page": "index"})
def index(page):
    # return render_template("index.html")
    return "Hello"
