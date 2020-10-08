# -*- coding: utf-8 -*-
__author__ = 'p2lly'

import requests
from web_app.models import Rates
from web_app import db
from web_app.models import currency_list


def get_currency_list(base_currency):
    url = f'https://api.exchangeratesapi.io/latest?base={base_currency}'
    response = requests.get(url)
    rates = response.json()

    return rates['rates']


def insert_rate(base, conversion, rate):
    r = Rates(base, conversion, rate)
    db.session.add(r)
    db.session.commit()


def first_fill_rates():
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


def get_currency_info(base, conversion):
    rate = Rates.query.filter_by(base_currency=base,
                                 conversion_currency=conversion).first()

    return rate


def refresh_rate(base, conversion, new_rate):
    currency = get_currency_info(base=base, conversion=conversion)

    if currency:
        currency.rate = new_rate
        db.session.add(currency)
        db.session.commit()


async def refresh_rates_schd():
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
    # get_currency_info(base='USD', conversion='EUR')
    # refresh_rate(base='USD', conversion='EUR', new_rate=2.0)
    # refresh_rate(base='EUR', conversion='PLN', new_rate=10.0)
    # get_currency_info(base='USD', conversion='EUR')
    # get_currency_info(base='EUR', conversion='PLN')
    # refresh_rates_schd()
    pass