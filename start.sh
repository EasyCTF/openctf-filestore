#!/bin/bash
set -e

service nginx start

if [ "$ENV" == "development" ]; then
	exec bash -c "DATABASE_URL=$DATABASE_URL python app.py"
else
	exec bash -c "DATABASE_URL=$DATABASE_URL gunicorn --bind 0.0.0.0:8000 -w 4 app:app"
fi
