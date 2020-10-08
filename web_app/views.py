# -*- coding: utf-8 -*-
__author__ = 'p2lly'

from flask import render_template
from web_app import app
from web_app.src.forms import InputDataForms
from web_app.src.currency import (
    get_currency_info,
)

currency_url = 'https://api.exchangeratesapi.io/latest?base={}'


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.route('/', methods=['GET', 'POST'])
def home():
    forms = InputDataForms()
    currency_data = dict()
    rate = 1.0

    if forms.validate_on_submit():
        first_currency = forms.first_currency.data
        second_currency = forms.second_currency.data
        convert_quantity = forms.quantity.data

        currency_data['first_currency'] = first_currency
        currency_data['second_currency'] = second_currency
        currency_data['qty'] = convert_quantity

        info = get_currency_info(first_currency, second_currency)

        if not info:
            pass
        else:
            rate = info.rate

        result = round(convert_quantity * rate, 2)
        currency_data['result'] = result

        app.logger.info(first_currency)
        app.logger.info(second_currency)
        app.logger.info(convert_quantity)
        app.logger.info(info)
        app.logger.info(result)

    return render_template('home.html', form=forms, data=currency_data)
