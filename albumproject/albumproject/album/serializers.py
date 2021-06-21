from rest_framework import serializers
from .models import Album, Comment, Genre
class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = [
            "id",
            "album_description", 
            "album_name", 
            "album_release",
            "album_time",
            "artist_name",
            "album_genre",
            "album_image",
        ]
# class DetailSerializer() use RetrieveAPI. Read REST documentation.

class DetailSerializer():
    class Meta:
        model = Album
        fields = [
            "id",
            "album_description", 
            "album_name", 
            "album_release",
            "album_time",
            "artist_name",
            "album_genre",
            "album_image",
            "comment_date",
            "comment_social",
            "track_number",
            "track_name",
            "track_time"
        ]