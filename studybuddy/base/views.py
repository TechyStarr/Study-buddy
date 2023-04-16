from django.shortcuts import render

# Create your views here.

rooms = [
    {'id': 1, 'name': "Let's learn Python together!"},
    {'id': 2, 'name': "Design with me"},
    {'id': 3, 'name': "Let's learn React"},
    {'id': 4, 'name': "Let's learn Django"},
    {'description': "This is a room for Python learners. Feel free to ask questions and help others."}
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = None
    for r in rooms:
        if r['id'] == int(pk):
            room = r

    context = {'room': room}

    return render(request, 'base/room.html', context)
