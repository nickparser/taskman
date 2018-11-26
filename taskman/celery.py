import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tm.settings')

app = Celery('mysite')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(packages=None)