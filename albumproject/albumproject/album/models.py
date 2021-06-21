from django.db import models
from django.urls import reverse
# Create your models here.
class Album(models.Model):
    album_image = models.ImageField(upload_to = "album", default = r'C:\Users\jlwil\albumproject\albumproject\albumproject\album\defaultimage.jpg')
    album_description = models.TextField(max_length=400)
    album_name = models.CharField(max_length=200)
    album_release = models.DateField()
    album_time = models.CharField(max_length=200)
    artist_name = models.CharField(max_length=200)
    album_genre = models.CharField(max_length=20, default = "pop")

    def __str__(self):
        return "{}".format(self.album_name)

    def get_absolute_url(self):
        return reverse("album_detail", kwargs = {'pk' : self.id})

class Comment(models.Model):
    comment_date = models.DateField(auto_now_add=True)
    comment_social = models.TextField(max_length=1000)
    album = models.ForeignKey(Album, on_delete = models.CASCADE)

    def __str__(self):
        return self.comment_social

class Genre(models.Model):
    genre_name = models.CharField(max_length = 15)
    album = models.ForeignKey(Album, on_delete = models.CASCADE)
    
class Tracks(models.Model):
    track_number = models.CharField(max_length = 510)
    track_name = models.CharField(max_length = 100)
    track_time = models.CharField(max_length = 25)
    album = models.ForeignKey(Album, on_delete = models.CASCADE)
