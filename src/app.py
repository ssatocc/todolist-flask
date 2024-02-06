import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config=None):
    app = Flask(__name__)

    if config is None:
        db_url = "sqlite:///" + os.path.join(os.path.dirname(__file__), "db.sqlite3")
        config = {
            "SQLALCHEMY_DATABASE_URI": db_url,
            "SQLALCHEMY_TRACK_MODIFICATIONS": False,
        }
    app.config.update(config)

    db.init_app(app)

    from models import Todo  # noqa

    @app.route("/", methods=["GET"])
    def index():
        return render_template("index.html")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=3000)
