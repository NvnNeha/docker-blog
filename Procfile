release: python manage.py migrate --noinput
web: gunicorn my_blog.wsgi --bind 0.0.0.0:${PORT:-8000} --workers ${WEB_CONCURRENCY:-2} --threads ${WEB_THREADS:-4} --worker-class gthread --timeout ${GUNICORN_TIMEOUT:-60} --graceful-timeout 30 --keep-alive 5 --max-requests 500 --max-requests-jitter 50 --preload --access-logfile - --error-logfile -
