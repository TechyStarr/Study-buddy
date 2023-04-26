from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serializers import RoomSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET/api',
        'GET/api/rooms',
        'GET/api/rooms/:id',
    ]
    return Response(routes) # safe=False allows for lists to be returned


@api_view(['GET'])
def get_rooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True) # many=True allows for multiple objects to be returned
    return Response(serializer.data)
    

@api_view(['GET'])
def get_room(request, pk):
    rooms = Room.objects.get(id=pk)
    serializer = RoomSerializer(rooms, many=False) # many=True allows for multiple objects to be returned
    return Response(serializer.data)


