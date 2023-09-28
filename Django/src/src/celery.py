from __future__ import absolute_import, unicode_literals

import os
from django.conf import settings
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')

app = Celery('src')
app.conf.enable_uts = False
app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object(settings, namespace='CELERY')

# celery beat settings
app.conf.beat_schedule = {
    'send-mail-in-every-2-min':{
        'task': 'demo.tasks.send_email',
        'schedule' : crontab(hour=12, minute=11),  
        'args': ('nandani@simformsolutions.com',),
    }
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')