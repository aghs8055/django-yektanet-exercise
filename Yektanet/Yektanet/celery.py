import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Yektanet.settings')
app = Celery('Yektanet')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


app.conf.beat_schedule = {
    'create_hourly_report': {
        'task': 'hourly_report',
        'schedule': crontab(minute=0, hour='*/1')
    },
    'create_daily_report': {
        'task': 'daily_report',
        'schedule': crontab(minute=0, hour=0)
    }
}
