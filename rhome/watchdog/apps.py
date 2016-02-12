from django.apps import AppConfig


class WatchdogConfig(AppConfig):
    name = 'rhome.watchdog'

    def ready(self):
        import rhome.watchdog.handlers  # noqa
