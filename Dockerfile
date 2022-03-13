FROM python:3.9.10-alpine

WORKDIR /app

ADD . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uwsgi", "app.ini"]
