from django.apps import AppConfig
from src.updater import activate_tread


class BeckendPageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'beckend_page'

    def ready(self):
        activate_tread()
