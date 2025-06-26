from generalnews.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'generalnews.db.models.BigAutoField'
    name = 'main'
