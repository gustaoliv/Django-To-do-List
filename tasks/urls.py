from django.urls import path
from .views import ListTasks, adiciona_tarefa, TaskDeleteView


urlpatterns = [
    path('', ListTasks.as_view(), name='lista-tarefas'),
    path('adicionar', adiciona_tarefa, name="adiciona_tarefa"),
    path('deletar/<int:pk>/', TaskDeleteView.as_view(), name="deletar-task"),
]