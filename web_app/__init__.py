# -*- coding: utf-8 -*-
__author__ = 'p2lly'


from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


from web_app import views, models
