FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7


RUN apt-get update && apt-get install python3-dev libevent-dev -y
RUN apt-get update && apt-get install --reinstall build-essential g++ -y


ENV TIMEOUT=300

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN python -m pip install -r requirements.txt
COPY openssl.cnf /etc/ssl/
COPY . .



EXPOSE 80
