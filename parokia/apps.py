from django.apps import AppConfig


class ParokiaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'parokia'
    verbose_name = 'Parokia dan Komox'

    def ready(self):
        import parokia.signals
