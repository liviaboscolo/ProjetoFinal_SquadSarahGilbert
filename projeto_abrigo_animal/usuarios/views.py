from django.shortcuts import render
from usuarios.forms import CadastroForm,LoginForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login

def cadastro_pessoa(request):
    form = CadastroForm()  # Cria uma instância do formulário

    if request.method == 'POST':
        form = CadastroForm(request.POST, request.FILES)  # Cria uma instância do formulário 
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    
    return render(request, 'cadastro_pessoa.html',{'form': form})

def login(request):
    form = LoginForm()  # Cria uma instância do formulário 
    if request.method == 'POST':
       form = LoginForm(request.POST)  # Cria uma instância do formulário 
       if form.is_valid():
           user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
           if user is None:
               form.add_error(None, 'Usuário ou senha inválidos. Tente novamente.') 
           else:
               login(request,user)
               return HttpResponseRedirect('/')
           
    return render(request, 'login.html',{'form': form})