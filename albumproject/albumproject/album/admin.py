from django.contrib import admin
from .models import Album, Comment, Tracks
# Register your models here.
class CommentInLine(admin.TabularInline):
    model = Comment

class TrackInLine(admin.TabularInline):
    model = Tracks

class AlbumAdmin(admin.ModelAdmin):
    inlines = [CommentInLine, TrackInLine]
    list_listplay = ["__str__"]
    class Meta:
        model = Album
        
admin.site.register(Album, AlbumAdmin)