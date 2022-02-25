from django.urls import path
from .views import ListTasks


urlpatterns = [
    path('', ListTasks.as_view(), name='lista-tarefas'),
]