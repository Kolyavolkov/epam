#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template, request
import requests
import psycopg2

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    name = os.environ["USER"]
    if request.method == "POST":
        city = request.form["city"]
        country = request.form["country"]
        api_key = os.environ["API_KEY"]
        url = ("http://api.openweathermap.org/data/2.5/"
              f"weather?appid={api_key}&q={city},{country}&units=metric")
        weather_url = requests.get(url)
        weather_data = weather_url.json()

        temp = round(weather_data["main"]["temp"])
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]
        write_db(country, city, temp)
        return render_template("result.html", temp=temp, humidity=humidity,
                                wind_speed=wind_speed, city=city)
    return render_template("index.html", name=name)


con = psycopg2.connect(
    host="postgres",
    database=os.environ["POSTGRES_USER"],
    user=os.environ["POSTGRES_USER"],
    password=os.environ["POSTGRES_PASSWORD"],
    port=5432
    )


@app.before_first_request
def create_table():

    cur = con.cursor()

    sql = '''CREATE TABLE IF NOT EXISTS Weather(
            Id SERIAL PRIMARY KEY,
            COUNTRY VARCHAR(40),
            CITY VARCHAR(40),
            TEMP INT)'''

    cur.execute(sql)
    con.commit()
    cur.close()


def write_db(country, city, temp):

    cur = con.cursor()

    data = "INSERT INTO weather VALUES(DEFAULT, '%s','%s','%s');" % (
        country, city, temp)
    cur.execute(data)
    con.commit()
    cur.close()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
