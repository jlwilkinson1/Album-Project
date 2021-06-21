from django.db import models
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from django.shortcuts import render
from .models import Album, Comment, Tracks
from .serializers import AlbumSerializer
# Create your views here.

class AlbumListView(ListView):
    model = Album

class AlbumDetailView(DetailView):
    model = Album

    #def get_context_data(self, *args, **kwargs):
    #    context = super(AlbumDetailView ,self).get_context_data(*args, **kwargs)
    #    album = Album.objects.get(pk = self.kwargs.get("pk"))
    #    tracks = Tracks.objects.filter(album=album)
    #    context ["album_detail"] = album
    #    context ["track_names"] = tracks
    #    context ["my_message"] = "hello world"
    #    return context
class GenreView(ListView):
    model = Album
    template_name = "albums/genres_detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(GenreView, self).get_context_data(*args, **kwargs)
        genre =  self.request.GET.get("value")
        queryset = Album.objects.filter(album_genre = genre)
        print(queryset)
        context ["this_list"] = queryset
        return context

class TrackListView(ListView):
    model = Album
    template_name = "albums/album_detail.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super(TrackListView, self).get_context_data(*args, **kwargs)
        track =  self.request.GET.get("value")
        queryset = Album.objects.filter(tracks_list = track)
        context ["track_list"] = queryset
        return context

class CommentCreateView(CreateView):
    model = Album
    fields = ["comment_social"]


class AlbumListAPIView(ListAPIView):
    model = Album
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class AlbumDetailAPIView(RetrieveAPIView):
    model = Album
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer