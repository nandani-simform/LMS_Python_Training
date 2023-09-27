from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class TaskListCreateView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers

class TaskRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all() 
    serializer_class = TaskSerializers   



