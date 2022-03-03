# Generated by Django 4.0.2 on 2022-03-03 21:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Data de Criação')),
                ('modified', models.DateField(auto_now=True, verbose_name='Data de atualização')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Data de Criação')),
                ('modified', models.DateField(auto_now=True, verbose_name='Data de atualização')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('name', models.CharField(max_length=150, verbose_name='Nome')),
                ('conclusion_date', models.DateField(verbose_name='Data de Conclusão')),
                ('file', models.FileField(blank=True, upload_to='uploads/', verbose_name='Arquivo')),
                ('description', models.TextField(max_length=400, verbose_name='Descrição')),
                ('done', models.BooleanField(default=False, verbose_name='Feito?')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.category')),
            ],
            options={
                'verbose_name': 'Tarefa',
                'verbose_name_plural': 'Tarefas',
            },
        ),
    ]
