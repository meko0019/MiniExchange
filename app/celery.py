from celery import Celery

celery = Celery('app')
celery.config_from_object('app.celeryconfig')