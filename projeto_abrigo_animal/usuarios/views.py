from django.shortcuts import render, get_object_or_404
from usuarios.forms import cadastro_forms
from django.http import HttpResponseRedirect
from .models import CustomUser


def cadastro_pessoa(request):
    form = cadastro_forms()  # Cria uma instância do formulário

    if request.method == 'POST':
        form = cadastro_forms(request.POST, request.FILES)  # Cria uma instância do formulário 
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    
    return render(request, 'cadastro_pessoa.html',{'form': form})
