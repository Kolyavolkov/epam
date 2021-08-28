A simple distributed weather application running across multiple Docker containers
with Postgresql database and pgadmin to access db with web interface.
[![Build Status](https://app.travis-ci.com/Kolyavolkov/epam.svg?branch=master)](https://app.travis-ci.com/Kolyavolkov/epam)
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

---
Licensing

MIT license

Copyright (c) [2021] [Volkov Nikolai]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
