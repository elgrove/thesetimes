from flask import Blueprint, render_template
from sqlalchemy.orm import Session
from sqlalchemy import desc
from .engine import get_engine
from .models import Article

core = Blueprint(
    "core",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/core",
)


ENGINE = get_engine()

# TODO scoped session


@core.route("/")
def home():
    with Session(ENGINE) as session:
        articles = (
            session.query(Article)
            .order_by(desc(Article.published_date))
            .limit(60)
            .all()
        )
    return render_template("home.html", articles=articles)


@core.route("/article/<id>")
def article(id):
    with Session(ENGINE) as session:
        article = session.query(Article).filter(Article.id == id).first()
    return render_template("article.html", article=article)
