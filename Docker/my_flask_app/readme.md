A simple distributed weather application running across multiple Docker containers
with Postgresql database and pgadmin to access db with web interface.
===

Getting started
---

Download [Docker Desktop](https://www.docker.com/products/docker-desktop) for Mac or Windows. [Docker Compose](https://docs.docker.com/compose) will be automatically installed. On Linux, make sure you have the latest version of [Compose](https://docs.docker.com/compose/install/).

Before running docker-compose you should create .env file inside app folder and specify
environment variables.

Copy your api key from [Openweather](https://openweathermap.org/api)
```
API_KEY=****
```
Provide your email and password to access pgadmin
```
PGADMIN_DEFAULT_EMAIL=example@gmail.com
PGADMIN_DEFAULT_PASSWORD=password
```
The app will greet you with defined name.
```
USER=NIKOLAI
```

Postgres will create database and user named $POSTGRES_USER
```
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
```

After that run docker compose from app directory with command
```
docker-compose --env-file .env up -d 
```

App runs at localhost:5000
Pgadmin runs at localhost:5050
---

To connect to database go to localhost:5050, entry e-mail & password.
Create new connection with server:
  - hostname should be "postgres"
  - database $POSTRES_USER
  - user $POSTGRES_USER
  - password $POSTGRES_PASSWORD
