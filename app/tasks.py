from time import sleep

from django.utils import timezone
from django.utils.lorem_ipsum import paragraph as get_random_paragraph

from .celery import app
from .models import Report


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


@app.task
def calculate_report_data(report_id):
    report = Report.objects.get(id=report_id)
    sleep(10)
    report.data.update({
        'text': get_random_paragraph()
    })
    report.date_completed = timezone.now()
    report.save()