from generalnews.apps import AppConfig


class NewsConfig(AppConfig):
    default_auto_field = 'generalnews.db.models.BigAutoField'
    name = 'news'
