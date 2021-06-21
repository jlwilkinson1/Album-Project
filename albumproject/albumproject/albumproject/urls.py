"""albumproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from album.views import(
                        AlbumListView,
                        AlbumDetailView,
                        GenreView,
                        TrackListView,
                        AlbumListAPIView,
                        AlbumDetailAPIView
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', AlbumListView.as_view(), name = "album_list"),
    path('albumdetail/<int:pk>/', AlbumDetailView.as_view(), name = "album_detail"),
    path('tracks/', TrackListView.as_view(template_name="album/album_detail.html"),kwargs = { "value" : "" }, name = "track_list"),
    path('genre/', GenreView.as_view(template_name="album/genres_detail.html"), kwargs = { "value" : "" }, name = "get_by_genre"),
    path('api/albumlist/', AlbumListAPIView.as_view(), name = "api_album_list"), #api, by convention starts with 'api'
    path('api/albumdetail/<int:pk>/', AlbumDetailAPIView.as_view(), name = "api_detail_list")

] 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)