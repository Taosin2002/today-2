from django.urls import path,include
from .import views
urlpatterns = [
    path('Album/',views.add_album,name='album'),
]