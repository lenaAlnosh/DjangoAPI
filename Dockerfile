# Use an official Python runtime as a parent image
FROM python:3.8

# Prevent Python from buffering stdout and stderr (recommended for Docker)
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /code
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD python manage.py runserver 0.0.0.0:80