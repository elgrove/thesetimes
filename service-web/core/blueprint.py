from flask import Blueprint, render_template
from sqlalchemy.orm import Session
from sqlalchemy import desc
from core.engine import get_engine
from thesetimes_orm.models import Article

core = Blueprint(
    "core",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/core",
)


@core.route("/")
def home_page():
    """Route for the root homepage."""
    with Session(get_engine()) as session:
        latest_articles = (
            session.query(Article)
            .order_by(desc(Article.page_rank))
            .order_by(desc(Article.published_date))
            .limit(40)  # TODO order by desc 20 is leaving out older aeticle from NYR
            .all()
        )
    top_articles = sorted(latest_articles, key=lambda x: x.page_rank)
    return render_template("home.html", articles=top_articles)


@core.route("/latest")
def latest_page():
    """Route for the root homepage."""
    with Session(get_engine()) as session:
        latest_articles = (
            session.query(Article)
            .order_by(desc(Article.published_date))
            .limit(40)
            .all()
        )
    return render_template("home.html", articles=latest_articles)


@core.route("/article/<uuid>")
def article_page(uuid):
    """Route to retrieve an individual article by uuid column."""
    with Session(get_engine()) as session:
        article = session.query(Article).filter(Article.uuid == uuid).first()
    return render_template("article.html", article=article)


@core.route("/publication/<short_name>")
def publication_page(short_name):
    """Route to retrieve a homepage for a specific publication, sorted by latest."""
    # TODO sort by day then by page rank
    with Session(get_engine()) as session:
        articles = (
            session.query(Article)
            .where(Article.publication_short == short_name)
            .order_by(desc(Article.published_date))
            .limit(40)
            .all()
        )
    return render_template("home.html", articles=articles)


@core.route("/<short_name>")
def publication_page(short_name):
    """Route to retrieve a homepage for a specific publication, sorted by latest."""
    # TODO sort by day then by page rank
    with Session(get_engine()) as session:
        articles = (
            session.query(Article)
            .where(Article.publication_short == short_name)
            .order_by(desc(Article.published_date))
            .limit(40)
            .all()
        )
    return render_template("home.html", articles=articles)
