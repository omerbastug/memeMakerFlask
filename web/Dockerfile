# syntax=docker/dockerfile:1

FROM python:3.10

WORKDIR /python-docker-new

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# python app.py
CMD gunicorn --bind 0.0.0.0:5000 -w 3 app:app