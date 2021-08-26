CI/CD pipeline script
===
To use this script you have to create .env file and define variables.
---
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
After that open epam_pipe.sh and specify variables
```
REPO="URL to your github repository"
PIPE="Directory where you want to clone remote repo"
APP_FILE="Python file that have to be checked by pylint"
BUILD_DIR="Directory where is your app with docker file"
SECRET="path to .env file that you created"