from .models import Task
from .serializers import TaskSerializers
# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def taskcreate (request):
    serializer=TaskSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response (serializer.data)


@api_view(['GET'])
def tasklist (request):
    tasks=Task.objects.all()
    serializer=TaskSerializers(tasks,many=True)
    return Response (serializer.data)


@api_view(['GET'])
def taskget (request,pk):
    tasks=Task.objects.get(id=pk)
    serializer=TaskSerializers(tasks,many=False)
    return Response (serializer.data)


@api_view(['POST'])
def taskupdate (request,pk):
    tasks=Task.objects.get(id=pk)
    serializer=TaskSerializers(instance=tasks,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response (serializer.data)


@api_view(['DELETE'])
def taskdelete (request,pk):
    tasks=Task.objects.get(id=pk)
    tasks.delete()
    return Response('done')