import subprocess
from functools import partial

from django.conf import settings
from django.utils import autoreload
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Run celery process'

    @staticmethod
    def _restart_process(command):
        subprocess.run(['pkill', 'celery'], check=False)
        subprocess.run(['celery', '-A', 'app.celery.app', command], check=False)

    def add_arguments(self, parser):
        parser.add_argument('command', choices=['worker', 'beat'])

        parser.add_argument(
            '--no-reload',
            action='store_true',
            help='Do not reload celery on code change',
        )

    def handle(self, *args, **options):
        command = partial(self._restart_process, options['command'])

        if options['no_reload']:
            command()
        else:
            autoreload.run_with_reloader(command)
