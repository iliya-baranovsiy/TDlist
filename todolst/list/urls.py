from django.urls import path, include
from .views import head_page, ToDoViewSet, todo_detail
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'todo', ToDoViewSet)

urlpatterns = [
    path('', head_page, name='head_page'),
    path('', include(router.urls)),
    path('todo/<int:id>/', todo_detail, name='todo_detail')
]
