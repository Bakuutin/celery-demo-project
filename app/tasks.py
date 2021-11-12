from .celery import app

from time import sleep


@app.task(bind=True)
def debug_task(self):
    """
    The bind argument means that the function will be a “bound method”
    so that you can access attributes and methods on the task type instance.
    """
    print(f'Request: {self.request!r}')


@app.task
def long_task():
    sleep(10)
    return 42


@app.task
def add(a, b):
    return a + b
