#!/bin/sh
python wait-for && python manage.py collectstatic --noinput && python manage.py migrate
exec "$@"
