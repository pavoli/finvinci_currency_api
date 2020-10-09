# -*- coding: utf-8 -*-

__author__ = 'p2lly'
__version__ = '1.0'


from web_app.models import Rates


base = 'USD'
conversion = 'EUR'
rate = 1.0


def test_rates_init():
    r = Rates(base=base, conversion=conversion, rate=rate)

    assert r.base_currency == base
    assert r.conversion_currency == conversion
    assert r.rate == rate


def test_rates_repr():
    r = Rates(base=base, conversion=conversion, rate=rate)
    assert 'Base rate: {0}|Conversion rate: {1}|Rate: {2}'.format(base,
                                                                  conversion,
                                                                  rate) == str(
        r)
