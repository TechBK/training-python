#!/bin/bash -e

if [ -f .venv/bin/activate ]; then
    echo   "Load Python virtualenv from '.venv/bin/activate'"
    source .venv/bin/activate
fi

gunicorn -b unix:var/run/gunicorn.sock main:app
