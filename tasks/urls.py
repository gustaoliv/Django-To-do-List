from django.urls import path
from .views import adiciona_tarefa, TaskDeleteView, adiciona_categoria, TaskUpdateView, index


urlpatterns = [
    path('', index, name='lista-tarefas'),
    path('adicionar', adiciona_tarefa, name="adiciona_tarefa"),
    path('check-task/<int:id>', index, name='check-task'),
    path('deletar/<int:pk>/', TaskDeleteView.as_view(), name="deletar-task"),
    path('editar/<int:pk>/', TaskUpdateView.as_view(), name="editar-task"),
    path('adicionar-categoria', adiciona_categoria, name='adiciona-categoria')
]