from django.urls import path, include
from .views import head_page, ToDoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'todo', ToDoViewSet)

urlpatterns = [
    path('', head_page, name='head_page'),
    path('', include(router.urls)),
]
