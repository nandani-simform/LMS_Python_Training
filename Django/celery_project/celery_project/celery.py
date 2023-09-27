from celery import Celery
import os
from celery.schedules import crontab
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_project.settings')

# celery beat settings
app = Celery('celery_project')

app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object(settings, namespace='CELERY')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'send-mail-in-every-3-min':{
        'task': 'demo.task.send_email',
        'schedule' : crontab(hour = 11, minute=55),  
        'args': (3,) 
    
      
    }
}
# app.conf.timezone = 'Asia/Kolkata'