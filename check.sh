#!/bin/bash

isort src/
black src/
flake8 src/
mypy src/
