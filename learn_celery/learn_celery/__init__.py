# The below code will help to recognize celery app in django 
# basically this help django to know the celery

from .celery import app as celery_app

__all__= ("celery_app",)