from typing import List
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Task


class ListTasks(ListView):
    model = Task
    template_name = 'tasks-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context