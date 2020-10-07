# -*- coding: utf-8 -*-
__author__ = 'p.olifer'


'''

'''

from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dadjahgdjagjdgsjkt63827fbg'

from web_app import views, models