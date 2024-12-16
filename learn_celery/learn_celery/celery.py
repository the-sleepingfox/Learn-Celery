import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learn_celery.settings')
app= Celery("learn_celery")
app.config_from_object("django.conf:settings", namespace= "CELERY")
app.conf.task_routes= {
    'testapp.tasks.task1': {
        'queue': 'queue1'
    },
    'taskapp.tasks.task2': {
        'queue': 'queue2'
    }
}
app.autodiscover_tasks()