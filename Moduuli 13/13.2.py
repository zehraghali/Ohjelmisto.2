import mysql.connector
import mysql.connector
import json

from flask import Flask, Response

app = Flask(__name__)

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user= 'root',
    password='zehra123',
    automcommit=True
    )

"SELECt name FROM airport WHERE iso_country =  'FI';"
@app.route("/kenttä/<icao>")
def haelentokenttaMaasta(icao):
    sql = f"SELECt name FROM airport WHERE iso_country = '{maa}';"
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)


