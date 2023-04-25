from django.apps import AppConfig


class CaloriesCounterConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "calories_counter"

    def ready(self):
        import calories_counter.signals
