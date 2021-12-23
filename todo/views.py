from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from todo.serializers import Taskserializer
from todo.models import Task
import requests

# Create your views here.
# @api_view(['GET'])
def home(request):
    info = requests.get('https://jsonplaceholder.typicode.com/users')
    data = info.json()
    return render(request, 'home.html', {'data': data})
    # context = {
    #     'All task': 'http://localhost:8000/all-task',
    #     'Create Task': 'http://localhost:8000/create-task',
    #     'Edit Task': 'http://localhost:8080/edit-task/id',
    #     'View Task': 'http://localhost:8080/view-task/id',
    #     'Delete Task': 'http://localhost:8080/delete-task/id',
    # }
    # return Response(context)

@api_view(['POST'])
def createtask(request):
    record = Taskserializer(data=request.data)
    if record.is_valid():
        record.save()
    return Response(record.data)

@api_view(['GET'])
def alltask(request):
    record = Task.objects.all()
    record = Taskserializer(record, many=True)
    return Response(record.data)

@api_view(['DELETE'])
def deletetask(request, id):
    record = Task.objects.get(id=id)
    record.delete()
    return Response('Record deleted')


@api_view(['PUT'])
def edittask(request, id):
    record = Task.objects.get(id=id)
    serilizer = Taskserializer(data = request.data, instance=record)
    if serilizer.is_valid():
        serilizer.save()
        return Response(record.data)
        
        