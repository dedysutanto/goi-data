from django.apps import AppConfig


class BaptisConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'baptis'

    def ready(self):
        import baptis.signals
