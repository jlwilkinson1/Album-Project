from django.apps import AppConfig
from .models import Album

class AlbumConfig(AppConfig):
    name = 'album'

admin.site.register(Post, PostAdmin)
