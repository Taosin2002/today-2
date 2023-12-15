from django.shortcuts import render,redirect
from Musician.forms import MusicianForm
from Musician.models import Musician
# Create your views here.
def add_musician(request):
    if request.method=="POST":
        form=MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('musician')
    else:
        form=MusicianForm()
        return render(request,'add_musician.html',{'form':form})

def edit_musician(request,id):
    musician=Musician.objects.get(pk=id)
    form=MusicianForm(request.POST,instance=musician)
    if request.method=="POST":
        form=MusicianForm(request.POST,instance=Musician)
        if form.is_valid():
            form.save()
            return redirect('musician')

    return render(request,'add_musiciank.html',{'form':form})

def delete_musician(request,id):
    musician=Musician.objects.get(pk=id)
    musician.delete()
    return redirect('musician')
