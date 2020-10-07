# -*- coding: utf-8 -*-
__author__ = 'p.olifer'


from flask import render_template, flash
from web_app import app
from web_app.src.forms import InputDataForms
import requests


currency_url = 'https://api.exchangeratesapi.io/latest?base={}'


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.route('/', methods=['GET', 'POST'])
def home():
    forms = InputDataForms()

    if forms.validate_on_submit():
        first_currency = forms.first_currency.data
        second_currency = forms.second_currency.data
        convert_quantity = forms.quantity.data

        currency_data = dict()
        currency_data['first_currency'] = first_currency
        currency_data['second_currency'] = second_currency
        currency_data['qty'] = convert_quantity

        app.logger.info(first_currency)
        app.logger.info(second_currency)
        app.logger.info(convert_quantity)

        response = requests.get(currency_url.format(first_currency))
        app.logger.info(response)

        if (response.ok is False):
            flash(f'Error: {response.status_code}')
            flash(f"{response.json()['error']}")

            return render_template('home.html', form=forms)
        else:
            data = response.json()
            second_value = data['rates'][second_currency]
            result = round(convert_quantity * second_value, 2)

            currency_data['result'] = result

            app.logger.info(data)
            app.logger.info(second_value)
            app.logger.info(result)

            return render_template('home.html', form=forms, data=currency_data)