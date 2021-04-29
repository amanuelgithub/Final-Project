from django.apps import AppConfig


class TrafficreportConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'TrafficReport'

    def ready(self):
        import TrafficReport.signals
