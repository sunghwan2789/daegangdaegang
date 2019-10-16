from django.shortcuts import render,get_object_or_404
from .models import Room
# Create your views here.
def info_me(request):
    rooms = Room.objects
    return render(request, 'info_me.html',{'rooms' : rooms})

def info_cul(request):
    rooms = Room.objects
    return render(request, 'info_cul.html',{'rooms' : rooms})

def info_na(request):
    rooms = Room.objects
    return render(request, 'info_na.html',{'rooms' : rooms})

def detail(request,room_id):
    room_detail = get_object_or_404(Room, pk=room_id)
    return render(request, 'detail.html', {'room':room_detail})

