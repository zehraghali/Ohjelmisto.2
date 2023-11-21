import json

from flask import Flask, Response

app = Flask(__name__)
@app.route('/summa/<luku>1/<luku2>')
def summa(luku1, luku2):
    try:
        summa = float(luku1)+float(luku2)
        tilakoodi: 200

        vastaus = {
        "luku1": luku1,
        "luku2": luku2,
        "summa": summa
        }

    except ValueError:
        tilakoodi: 400
        vastaus = {
            "status" : tilakoodi,
            "teksti": "Virheellinen syöte"

        }

    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, content_type="application/json")


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
