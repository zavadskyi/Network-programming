import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


def get_data():
    today = datetime.now()
    start_date = today - timedelta(days=today.weekday() + 7)
    end_date = start_date + timedelta(days=6)

    url = "https://bank.gov.ua/NBU_Exchange/exchange_site"
    params = {
        "start": start_date.strftime("%Y%m%d"),
        "end": end_date.strftime("%Y%m%d"),
        "valcode": "usd",
        "sort": "exchangedate",
        "order": "asc",
        "json": ""
    }

    response = requests.get(url, params=params)
    return response.json()


def draw_chart(data):
    dates = [item['exchangedate'] for item in data]
    rates = [item['rate'] for item in data]

    plt.figure(figsize=(10, 5))
    plt.plot(dates, rates, marker='o', color='green', label='USD')

    plt.title('Курс USD за минулий тиждень')
    plt.xlabel('Дата')
    plt.ylabel('Курс')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    plt.savefig('nbu_chart.png')
    plt.show()


if __name__ == "__main__":
    data = get_data()
    if data:
        draw_chart(data)