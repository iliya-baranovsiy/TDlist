from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import ToDo
from .serializer import ToDoSerializer
from django.http import JsonResponse, HttpResponseNotAllowed
import json


def head_page(request):
    if request.method == "POST":
        title = request.POST.get('text_input')
        if title:
            ToDo.objects.create(title=title)
            return redirect('head_page')
    todos = ToDo.objects.all()
    return render(request, "head.html", {'todos': todos})


class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.done = request.data.get('done', False)
        instance.title = request.data.get('title', instance.title)
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


def todo_detail(request, id):
    if request.method == 'DELETE':
        try:
            todo = ToDo.objects.get(id=id)
            todo.delete()
            return JsonResponse({'message': 'Deleted'}, status=204)
        except:
            return JsonResponse({'message': 'Todo not found'}, status=404)
    return HttpResponseNotAllowed(['DELETE'])


def todo_patch(request, id):
    if request.method == 'PATCH':
        try:
            todo = ToDo.objects.get(id=id)
            data = json.loads(request.body)
            if 'title' in data:
                todo.title = data['title']
            if 'done' in data:
                todo.done = data['done']
            todo.save()
            return JsonResponse({'id': todo.id, 'title': todo.title, 'done': todo.done}, status=200)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=400)

    return HttpResponseNotAllowed(['PATCH'])
