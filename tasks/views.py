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


@method_decorator(login_required(login_url='login'), name='dispatch')
class ListTasks(ListView):
    model = Task
    template_name = 'tasks-list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(author=self.request.user)
        return context

    def get_queryset(self):
        qs = self.model.objects.filter(author=self.request.user).order_by('done', 'conclusion_date')
        return qs


def adiciona_tarefa(request):
    name = request.POST.get('name')
    conclusion_date = request.POST.get('conclusion_date')
    category = request.POST.get('category')
    if request.POST.get('file'):
        file = request.POST.get('file')
    description = request.POST.get('description')

    form = TaskForm(request.POST)

    if form.is_valid():
        register = form.save(commit=False)
        register.author = request.user
        register.save()


    return redirect('lista-tarefas')



def adiciona_categoria(request):
    form = CategoryForm(request.POST)

    if form.is_valid():
        register = form.save(commit=False)
        register.author = request.user
        register.save()

    return redirect('lista-tarefas')
    

class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("lista-tarefas")

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Task, id=id_)



class TaskUpdateView(UpdateView):
    model = Task
    success_url = reverse_lazy("lista-tarefas")
    # fields = ['name', 'conclusion_date', 'category', 'file', 'description', 'done']
    fields = ['name',]