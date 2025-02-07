from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import ToDo
from .serializer import ToDoSerializer
from django.http import JsonResponse, HttpResponseNotAllowed


def head_page(request):
    if request.method == "POST":
        title = request.POST.get('text_input')
        if title:
            ToDo.objects.create(title=title)
            return redirect('head_page')  # Перенаправляем обратно на страницу после создания
    todos = ToDo.objects.all()  # Получаем все задания для отображения
    return render(request, "head.html", {'todos': todos})


class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.done = request.data.get('done', False)
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
