import requests
from flask import Flask, request
from datetime import datetime, timedelta

app = Flask(__name__)


@app.route("/currency")
def get_currency_nbu():
    dt = datetime.now()

    if "yesterday" in request.args:
        dt = dt - timedelta(days=1)

    date_str = dt.strftime("%Y%m%d")

    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
    params = {
        "valcode": "USD",
        "date": date_str,
        "json": ""
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        if data:
            rate = data[0]['rate']
            return f"USD {rate}"
        else:
            return "Курс не знайдено"
    else:
        return "Помилка API НБУ"


if __name__ == "__main__":
    app.run(port=8000)