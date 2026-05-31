# syntax=docker/dockerfile:1
FROM python:3.12-slim

# Keep Python lean and logs unbuffered for container output
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies first so they cache across code changes
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project
COPY . .

# Collect static files (Tailwind CSS is already built into theme/static).
# A throwaway SECRET_KEY is fine here — it's only used for the build step.
RUN SECRET_KEY=build-only-key DEBUG=False USE_S3=False \
    python manage.py collectstatic --noinput

EXPOSE 8000

# Apply migrations, then serve with gunicorn (whitenoise serves static files)
CMD ["sh", "-c", "python manage.py migrate --noinput && gunicorn my_blog.wsgi --bind 0.0.0.0:8000 --workers 2 --threads 4 --worker-class gthread --timeout 60 --access-logfile - --error-logfile -"]
