from typing import List
from unicodedata import name
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from .models import Task, Category
from .forms import TaskForm
from django.views.generic.edit import DeleteView

class ListTasks(ListView):
    model = Task
    template_name = 'tasks-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


def adiciona_tarefa(request):
    name = request.POST.get('name')
    conclusion_date = request.POST.get('conclusion_date')
    category = request.POST.get('category')
    if request.POST.get('file'):
        file = request.POST.get('file')
    description = request.POST.get('description')

    form = TaskForm(request.POST)

    if form.is_valid():
        form.save()

    return redirect('lista-tarefas')


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("lista-tarefas")

    
    
    
