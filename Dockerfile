FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD [ "gunicorn", "--workers", "1", "--bind", "0.0.0.0:80", "run:app" ]