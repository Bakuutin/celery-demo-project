from functools import partial

from django.db import transaction

import celery


def enqueue_on_commit(task: celery.Task, *args, **kwargs):
    transaction.on_commit(partial(task.apply_async, args, kwargs))
