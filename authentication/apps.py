from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'authentication'

    def ready(self):
        from . import signals
