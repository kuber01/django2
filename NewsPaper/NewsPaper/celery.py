import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPaper.settings')

app = Celery('NewsPaper')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'notify:':{
        'tasks': 'every_monday_notify',
        'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
        'args':()
    }
}