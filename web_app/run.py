# -*- coding: utf-8 -*-
__author__ = 'p2lly'


'''

'''


from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio
from web_app.src.currency import refresh_rates_schd
from web_app import app
app.run(host='0.0.0.0', port=5000, debug=True)


if __name__ == '__main__':
    scheduler = AsyncIOScheduler()
    scheduler.add_job(refresh_rates_schd, 'interval', hours=24)
    scheduler.start()
    try:
        asyncio.get_event_loop().run_forever()
    except (KeyboardInterrupt, SystemExit):
        pass