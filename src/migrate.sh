#!/bin/bash

rm -rf migrations/ db.sqlite3

export FLASK_APP=migrate.py
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
