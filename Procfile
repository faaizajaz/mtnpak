web: gunicorn MTNPAK.wsgi:application
release: python manage.py makemigrations; python manage.py migrate --noinput; python manage.py loaddata grades.json; python manage.py loaddata auth_groups.json