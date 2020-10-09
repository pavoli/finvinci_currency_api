# -*- coding: utf-8 -*-
__author__ = 'p2lly'

import requests
from web_app.models import Rates
from web_app import db
from web_app.models import currency_list


def get_currency_list(base_currency: str) -> dict:
    url = f'https://api.exchangeratesapi.io/latest?base={base_currency}'
    response = requests.get(url)
    rates = response.json()

    return rates['rates']


def insert_rate(base: str, conversion: str, rate: float) -> None:
    r = Rates(base, conversion, rate)
    db.session.add(r)
    db.session.commit()


def first_fill_rates() -> None:
    currency = [i[0] for i in currency_list]
    for c in currency:
        data = get_currency_list(c)
        for i in data:
            if i in currency and i != c:
                params = [c, i, data[i]]
                insert_rate(*params)


def show_all_rates():
    rates = Rates.query.all()

    for r in rates:
        print(r)


def get_currency_info(base: str, conversion: str) -> Rates:
    rate = Rates.query.filter_by(base_currency=base,
                                 conversion_currency=conversion).first()

    return rate


def refresh_rate(base: str, conversion: str, new_rate: float) -> None:
    currency = get_currency_info(base=base, conversion=conversion)

    if currency:
        currency.rate = new_rate
        db.session.add(currency)
        db.session.commit()


def refresh_rates_scheduled() -> None:
    currency = [i[0] for i in currency_list]
    for c in currency:
        data = get_currency_list(c)
        for i in data:
            if i in currency and i != c:
                params = [c, i, data[i]]
                refresh_rate(*params)


if __name__ == '__main__':
    # get_currency_list('USD')
    # show_all_rates()
    # print(get_currency_info(base='USD', conversion='EUR'))
    # refresh_rate(base='USD', conversion='EUR', new_rate=2.0)
    # refresh_rate(base='EUR', conversion='PLN', new_rate=10.0)
    # print(get_currency_info(base='USD', conversion='EUR'))
    # print(get_currency_info(base='EUR', conversion='PLN'))
    # refresh_rates_scheduled()
    pass
