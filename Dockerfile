FROM python:3.9.6-slim-bullseye

WORKDIR /kindabyt

ADD . /kindabyt/

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=kindabyt_flask_app.py
ENV FLASK_ENV=development

CMD flask run --host 0.0.0.0

EXPOSE 5000
