FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN apt-get update && apt-get install -y gnupg2 apt-transport-https
RUN apt-get update && apt install curl -y
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list

RUN apt-get update && ACCEPT_EULA=Y apt-get install msodbcsql17 -y
RUN apt-get update && ACCEPT_EULA=Y apt-get install mssql-tools -y


RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc

RUN apt-get update && apt-get install unixodbc-dev -y
RUN apt-get update && apt-get install python3-dev libevent-dev -y
RUN apt-get update && apt-get install --reinstall build-essential unixodbc-dev g++ -y
# RUN apt-get update && apt install python3-pip -y

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN python -m pip install -r requirements.txt
COPY openssl.cnf /etc/ssl/
COPY . .

EXPOSE 80

#docker build -t novus-api .
#docker run -d --name novus-api -p 8068:80 novus-api
