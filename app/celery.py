import os
import json
import uuid

from celery import Celery

from kombu import serialization

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

app = Celery('app')
# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# # Load task modules from all registered Django apps.
app.autodiscover_tasks()


class ExtendedJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, uuid.UUID):
            return str(obj)
        return super().default(obj)


_encoder = ExtendedJSONEncoder()
serialization.register('json', _encoder.encode, json.loads, content_type='application/json')