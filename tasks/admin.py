from django.contrib import admin
from .models import Category, Task


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'author')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'done', 'author', 'conclusion_date', 'category', 'created')