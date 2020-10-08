# -*- coding: utf-8 -*-
__author__ = 'p2lly'
__version__ = '1.0'


from flask_wtf import FlaskForm
from wtforms import (
    FloatField,
    SelectField,
    SubmitField
)
from wtforms.validators import DataRequired
from web_app.models import currency_list


class InputDataForms(FlaskForm):
    first_currency = SelectField('first', choices=currency_list,
                                 validators=[DataRequired()])
    second_currency = SelectField('second', choices=currency_list,
                                  validators=[DataRequired()])
    quantity = FloatField('How much to convert?', validators=[DataRequired()])
    submit = SubmitField('Convert')
