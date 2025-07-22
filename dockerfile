# # Use official Python image
# FROM python:3.11-slim

# # Set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# # Set working directory
# WORKDIR /app

# # Install dependencies
# RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

# # Copy requirements and install
# COPY requirements.txt .
# RUN pip install --upgrade pip && pip install -r requirements.txt

# # Copy project files
# COPY . .

# # Collect static files (optional for admin panel)
# RUN python manage.py collectstatic --noinput || true

# # Expose port
# EXPOSE 8000

# # Start app (Railway will override if needed)
# CMD ["gunicorn", "sfyt_portfolio.wsgi:application", "--bind", "0.0.0.0:8000"]



#new 


FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput || true

EXPOSE 8000

CMD ["gunicorn", "sfyt_portfolio.wsgi:application", "--bind", "0.0.0.0:8000"]
