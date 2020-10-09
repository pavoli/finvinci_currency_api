# -*- coding: utf-8 -*-

__author__ = 'p2lly'
__version__ = '1.0'


from web_app.src.currency import *
from web_app.models import Rates


def test_get_currency_info_type():
    r1 = Rates(base='USD', conversion='EUR', rate=2.5)
    r2 = get_currency_info(base='USD', conversion='PLN')

    assert type(r1) == type(r2)


def test_get_currency_list_type():
    d1 = get_currency_list(base_currency='USD')
    d2 = dict()

    assert type(d1) == type(d2)


def test_refresh_rate():
    refresh_rate(base='USD', conversion='EUR', new_rate=2.0)
    r_after = get_currency_info(base='USD', conversion='EUR')
    r_expected = Rates('USD', 'EUR', 2.0)

    assert str(r_after) == str(r_expected)