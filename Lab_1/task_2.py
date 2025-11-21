import requests
from datetime import datetime, timedelta
import json


def get_previous_week_dates():

    today = datetime.now()
    current_weekday = today.weekday()

    days_to_last_monday = current_weekday + 7
    start_date = today - timedelta(days=days_to_last_monday)

    end_date = start_date + timedelta(days=6)

    return start_date, end_date


def get_nbu_data():
    start_date, end_date = get_previous_week_dates()
    start_str = start_date.strftime("%Y%m%d")
    end_str = end_date.strftime("%Y%m%d")

    print(f"DEBUG: Запит за період {start_str} - {end_str}")

    url = "https://bank.gov.ua/NBU_Exchange/exchange_site"
    params = {
        "start": start_str,
        "end": end_str,
        "valcode": "usd",
        "sort": "exchangedate",
        "order": "asc",
        "json": ""
    }

    try:
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Помилка: Сервер повернув код {response.status_code}")
            return []

    except requests.exceptions.RequestException as e:
        print(f"Критична помилка з'єднання: {e}")
        return []


if __name__ == "__main__":
    rates = get_nbu_data()

    if rates:
        print(f"\nОтримано записів: {len(rates)}")
        # Виводимо отримані дані у гарному форматі json
        print(json.dumps(rates, indent=4, ensure_ascii=False))
    else:
        print("Даних не отримано.")