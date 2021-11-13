from time import sleep
from datetime import timedelta

from django.utils import timezone
from django.utils.lorem_ipsum import sentence as get_random_sentence

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
    report.data.update({
        'text': get_random_sentence()
    })
    sleep(10)

    report.date_completed = timezone.now()
    report.save()


@app.task
def fix_empty_reports():
    now = timezone.now()

    for report_id in Report.objects.filter(
        date_requested__lt=now - timedelta(minutes=1),
        date_completed__isnull=True,
    ).values_list('id', flat=True):
        calculate_report_data.delay(report_id)