import os
import requests

url = "https://api.apilayer.com/exchangerates_data/latest"
API_KEY = os.getenv('exchange_API')


def get_currency_rate(currency: str):
    """Получает курс валюты к рублю из этих ваших интернатов"""
    headers = {
        "apikey": API_KEY
    }
    payload = {}
    base = currency
    symbols = "RUB"
    response = requests.request("GET", url, headers=headers, data=payload,
                                params={"symbols": symbols, "base": base})
    result = response.json()
    return result


print(get_currency_rate('USD'))
