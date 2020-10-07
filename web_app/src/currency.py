import requests


class CurrencyData():
    url = 'https://api.exchangeratesapi.io/latest?base=CZK'
    response = requests.get(url)
    print(response.json())