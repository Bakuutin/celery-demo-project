from importlib import import_module

from django.apps import AppConfig

default_app_config = 'app.CoreConfig'


class CoreConfig(AppConfig):
    name = 'app'

    def ready(self):
        # This will make sure the app is always imported when
        # Django starts so that shared_task will use this app.
        import_module('app.celery')
