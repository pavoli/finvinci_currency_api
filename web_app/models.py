# -*- coding: utf-8 -*-
__author__ = 'p2lly'


from web_app import db


currency_list = [
    ('USD', 'US Dollar'),
    ('EUR', 'Euro'),
    ('PLN', 'Polish zloty'),
    ('CZK', 'Czech crown'),
]


class Rates(db.Model):
    __tablename__ = 'master_rates'

    pk = db.Column(db.Integer, primary_key=True)
    base_currency = db.Column(db.String(3))
    conversion_currency = db.Column(db.String(3))
    rate = db.Column(db.Float)

    def __init__(self, base, conversion, rate):
        self.base_currency = base
        self.conversion_currency = conversion
        self.rate = rate


    def __repr__(self):
        return 'Base rate: {0}    Conversion rate: {1}     Rate: {2}'.format(
            self.base_currency, self.conversion_currency, self.rate)

