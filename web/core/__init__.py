from flask import Blueprint, render_template
from sqlalchemy.orm import Session
from sqlalchemy import desc
from .database import engine, models

core = Blueprint(
    "core",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/core",
)


ENGINE = engine.get_engine()


@core.route("/")
def home():
    with Session(ENGINE) as session:
        articles = (
            session.query(models.Article)
            .order_by(desc(models.Article.published_date))
            .limit(60)
            .all()
        )
    return render_template("home.html", articles=articles)
