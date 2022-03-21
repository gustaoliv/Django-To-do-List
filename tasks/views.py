import re
from typing import List
from unicodedata import name
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from .models import Task, Category
from .forms import TaskForm, CategoryForm
from django.views.generic.edit import DeleteView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required



login_required(login_url='login')
def index(request, id=None):
    if request.user == 'AnonymousUser':
        return redirect('login')
    tasks = Task.objects.filter(author=request.user).order_by('conclusion_date', 'done')
    categories = Category.objects.filter(author=request.user)
    context = {
        'tasks': tasks,
        'categories': categories,
    }
    if request.method == 'GET':
        return render(request, 'tasks-list.html', context)
    else:
        task = Task.objects.get(id=id)
        if task.done:
            task.done = False
        else:
            task.done = True
        task.save()
        return redirect('lista-tarefas')




login_required(login_url='login')
def adiciona_tarefa(request):
    context = {
        'categories': Category.objects.filter(author=request.user)
    }
    if request.method == 'GET':
        return render(request, 'add-task.html', context)
    else:
        form = TaskForm(request.POST)
        if form.is_valid():
            register = form.save(commit=False)
            register.author = request.user
            register.save()

        return redirect('lista-tarefas')


login_required(login_url='login')
def adiciona_categoria(request):

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            register = form.save(commit=False)
            register.author = request.user
            register.save()
        
        return redirect('adiciona_tarefa')
    else:
        form = CategoryForm(request.POST)

        
    
@method_decorator(login_required(login_url='login'), name='dispatch')
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete-task.html'
    success_url = reverse_lazy("lista-tarefas")

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Task, id=id_)


@method_decorator(login_required(login_url='login'), name='dispatch')
class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update-task.html'
    success_url = reverse_lazy("lista-tarefas")
    fields = ['name', 'conclusion_date', 'category', 'description', 'done']
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(author=self.request.user)
        return context


   