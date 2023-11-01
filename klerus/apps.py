from django.apps import AppConfig


class KlerusConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'klerus'

    def ready(self):
        import klerus.signals
