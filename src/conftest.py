import os

import pytest

from app import create_app, db


@pytest.fixture(scope="session")
def client():
    db_url = "sqlite:///" + os.path.join(os.path.dirname(__file__), "db_pytest.sqlite3")
    config = {
        "SQLALCHEMY_DATABASE_URI": db_url,
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
        "TESTING": True,
    }
    app = create_app(config)
    client = app.test_client()

    with app.app_context():
        db.create_all()
        yield client
        db.drop_all()
