# -*- coding: utf-8 -*-
__author__ = 'p2lly'


import os


CSRF_ENABLED = True
SECRET_KEY = 'dadjahgdjagjdgsjkt63827fbg'

basedir = os.path.abspath(os.path.dirname(__file__))
db_name = 'currency_rates.db'

#SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(basedir, db_name) # mac os x
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, db_name) # win version
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False
