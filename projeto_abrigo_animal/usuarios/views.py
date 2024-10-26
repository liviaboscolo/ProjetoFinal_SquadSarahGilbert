from django.shortcuts import render, get_object_or_404
from usuarios.forms import CustomUserCreationForm
from .models import CustomUser
def cadastro_pessoa(request):
    form = CustomUserCreationForm # Cria uma instância do formulário
    pessoas = CustomUser.objects.all()  # Recupera todos os animais do banco de dados
    return render(request, 'cadastro_pessoa.html', {'form': form})
        