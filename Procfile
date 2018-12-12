release: python manage.py createsuperuser
release: python manage.py migrate
web: gunicorn InstaZen.wsgi --log-file -