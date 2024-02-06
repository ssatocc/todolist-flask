import os
from datetime import datetime

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

from validators import TodoValidator

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

    class Todo(db.Model):
        __tablename__ = "todos"

        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(50), nullable=False)
        completed = db.Column(db.Boolean, default=False)
        created_at = db.Column(db.DateTime, default=datetime.utcnow)
        updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    @app.route("/", methods=["GET"])
    def index():
        return render_template("index.html")

    @app.route("/api/todolist", methods=["GET"])
    def api_todolist_get():
        return jsonify(
            [
                {"id": todo.id, "name": todo.name, "completed": todo.completed}
                for todo in Todo.query.all()
            ]
        )

    @app.route("/api/todolist", methods=["POST"])
    def api_todolist_post():
        try:
            request_dict = request.get_json()
            todo_validator = TodoValidator(name=request_dict["name"])
            db.session.add(Todo(name=todo_validator.name))
            db.session.commit()
            return jsonify({"status": "success"})
        except Exception as ex:
            return jsonify({"status": "error", "message": str(ex)})

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=3000)
