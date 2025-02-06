from django.shortcuts import render
from rest_framework import viewsets
from .models import ToDo
from .serializer import ToDoSerializer


# Create your views here.

def head_page(request):
    return render(request, "head.html")


class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

