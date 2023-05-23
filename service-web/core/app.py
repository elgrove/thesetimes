from flask import Flask

from core.blueprint import core
from core.filters import print_date


def create_app():
    """App factory for the Flask app with configuration."""
    app = Flask(__name__)
    app.register_blueprint(core)
    app.add_template_filter(print_date, "date")
    return app


def start_development_server():
    """Run development server. For development purposes only."""
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=8000)
