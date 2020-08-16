web: gunicorn MTNPAK.wsgi:application
release: python manage.py makemigrations; python manage.py migrate --noinput; python manage.py loaddata grades.json