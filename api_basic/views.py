from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from todos.models import Todo
from .serializer import TodoSerializer
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def todolist(request):
    todo = Todo.objects.all()
    serializer = TodoSerializer(todo, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def todoDetail(request, id):
    todo = Todo.objects.get(id=id)
    serializer = TodoSerializer(todo, many=False)
    return Response(serializer.data)
 
@api_view(['POST'])
def todoCreate(request):
    serializer = TodoSerializer(data=request.data)

    if(serializer.is_valid()):
        serializer.save()
    return Response(serializer.data)      

@api_view(['PUT'])
def todoUpdate(request, id):
    todo = Todo.objects.get(id=id)
    serializer = TodoSerializer(instance=todo, data=request.data)
    if(serializer.is_valid()):
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def todoDelete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return Response('DELETED')
