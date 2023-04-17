from django.shortcuts import render, redirect
from .models import Room, Topic
from .forms import RoomForm

# Create your views here.

# rooms = [
#     {'id': 1, 'name': "Let's learn Python together!"},
#     {'id': 2, 'name': "Design with me"},
#     {'id': 3, 'name': "Let's learn React"},
#     {'id': 4, 'name': "Let's learn Django"},
# ]

def home(request):
    rooms = Room.objects.all()

    topics = Topic.objects.all()

    context = {'rooms': rooms, 'topics': topics}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}

    return render(request, 'base/room.html', context)

def create_room(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)


def update_room(request, pk):
    room = Room.objects.get(id=pk) # get the room to be updated
    form = RoomForm(instance=room) # pre-populate the form with the existing data

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room) # update the form with the new data
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {"form": form}
    return render(request, 'base/room_form.html', context)


def delete_room(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':

        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room} )


