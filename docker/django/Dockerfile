FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# 1. Copy the entire requirements folder
COPY requirements/ ./requirements/

# 2. Update pip and install from the specific subfolder path
RUN pip install --upgrade pip
RUN pip install -r requirements/dev.txt

# 3. Copy the rest of your ePBR project code
COPY . .

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]