from django.apps import AppConfig


class CreateUserConfig(AppConfig):
    """
    This class is responsible for creating user.
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "create_user"
