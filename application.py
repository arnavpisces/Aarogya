#gunicorn --bind 0.0.0.0 main:app
uwsgi --socket 0.0.0.0:8000 --protocol=http -w main:app
