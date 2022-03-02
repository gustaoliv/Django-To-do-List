from django.shortcuts import render
from .forms import CustomUserCreateForm
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import redirect, render



def CadastroView(request):
    context = {}
    if request.POST:
        form = CustomUserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Cadastro realizado com sucesso.')            
            return redirect('lista-tarefas')
        else:
            messages.error(request, 'Email ou senha inválidos.')
            context['registration_form'] = form

    else:
        form = CustomUserCreateForm()
        context['registration_form'] = form
    
    return render(request, 'signup.html', context)