from django.db import models
from django.contrib.auth import get_user_model


class Base(models.Model):
    created = models.DateField('Data de Criação', auto_now_add=True, blank=True)
    modified = models.DateField('Data de atualização', auto_now = True, blank=True)
    active = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Category(Base):
    name = models.CharField('Nome', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ('Categoria')
        verbose_name_plural = ('Categorias')

class Task(Base):
    author = models.ForeignKey(get_user_model(), verbose_name='Autor', on_delete=models.CASCADE)
    name = models.CharField('Nome', max_length=150)
    conclusion_date = models.DateField('Data de Conclusão')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    file = models.FileField('Arquivo', upload_to='uploads/', blank=True)
    description = models.TextField('Descrição', max_length=400)
    done = models.BooleanField('Feito?', default=False)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = ('Tarefa')
        verbose_name_plural = ('Tarefas')