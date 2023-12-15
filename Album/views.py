from django.shortcuts import render
from .forms import AlbumForm
# Create your views here.
def add_album(request):
    album=AlbumForm
    return render(request,'add_album.html',{'alb':album})