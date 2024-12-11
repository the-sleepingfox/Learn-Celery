import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learn_celery.settings')
app= Celery("learn_celery")
app.config_from_object("django.conf:settings", namespace= "CELERY")

@app.task
def add_number():
    return

app.autodiscover_tasks()