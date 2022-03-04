from django.urls import path
from .views import ListTasks, adiciona_tarefa, TaskDeleteView, adiciona_categoria, TaskUpdateView


urlpatterns = [
    path('', ListTasks.as_view(), name='lista-tarefas'),
    path('adicionar', adiciona_tarefa, name="adiciona_tarefa"),
    path('deletar/<int:pk>/', TaskDeleteView.as_view(), name="deletar-task"),
    path('editar/<int:pk>/', TaskUpdateView.as_view(), name="editar-task"),
    path('adicionar-categoria', adiciona_categoria, name='adiciona-categoria')
]