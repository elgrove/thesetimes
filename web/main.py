from flask import Flask
from core.blueprint import core

app = Flask(__name__)


from datetime import datetime


def print_date(dtobj):
    mapping = {"1": "st", "2": "th", "3": "rd"}
    try:
        suffix = mapping[str(dtobj.day)[-1]]
    except KeyError:
        suffix = "th"

    format = f"%H:%M, %-d{suffix} %B"
    return datetime.strftime(dtobj, format)


def create_app():
    app = Flask(__name__)
    app.register_blueprint(core)
    app.add_template_filter(print_date, "date")
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=8000)
