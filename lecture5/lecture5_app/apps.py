from tabnanny import verbose
from django.apps import AppConfig

class Lecture5AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lecture5_app'
    verbose_name = "Рассказы"
