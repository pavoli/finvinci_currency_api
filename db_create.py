# coding: utf-8
__author__ = 'p2lly'


'''
'''


import os
from config import (
    basedir,
    db_name,
)
from web_app import db
from web_app.src.currency import (
    first_fill_rates,
)

if not os.path.isfile(os.path.join(basedir, db_name)):
    db.create_all()
    first_fill_rates()
