# -*- coding: utf-8 -*-
__author__ = 'p2lly'


'''

'''


from apscheduler.schedulers.background import BackgroundScheduler
from web_app.src.currency import refresh_rates_scheduled
from web_app import app


scheduler = BackgroundScheduler()
scheduler.add_job(refresh_rates_scheduled, "interval", hours=24)
scheduler.start()

app.run(host='0.0.0.0', port=5000, debug=True)