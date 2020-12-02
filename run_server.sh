#!/bin/bash
export FLASK_APP=app.py
export FLASK_ENV=development # optional
flask run --host 0.0.0.0 --port 5000

# run in the background
#nohup flask run --host 0.0.0.0 --port 5000 >log.txt 2>&1 &