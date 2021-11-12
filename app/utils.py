from functools import partial
import uuid

from django.db import transaction

import celery


def enqueue_on_commit(task: celery.Task, *args, **kwargs):
    transaction.on_commit(partial(task.apply_async, args, kwargs))


import json

class ExtendedJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, uuid.UUID):
            return str(obj)
        return super().default(obj)

from kombu import serialization

_encoder = ExtendedJSONEncoder()

serialization.register(
    'json', _encoder.encode, json.loads,
    content_type='application/json',
)