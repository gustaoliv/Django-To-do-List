from django.forms import ModelForm
from .models import Task, Category


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'conclusion_date', 'category', 'file', 'description']



class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name',]