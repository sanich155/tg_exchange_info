import json
from datetime import datetime
from utils import get_currency_rate



def main():
    while True:
        user_currency = input('Введите валюту USD или EUR: ')

        currency_info = get_currency_rate(user_currency)
        rate = currency_info['rates']['RUB']
        timestamp = currency_info['timestamp']

        print(f'Курс {user_currency} к рублю: {rate}')

        with open ('data.json', 'w', encoding='utf-8') as f:
            data = {"Время запроса": timestamp,
                    "Валюта": user_currency,
                    "Курс валюты к рублю": rate,
                    }
            json.dump(data, f, ensure_ascii=False)
        break

if __name__ == '__main__':
    main()