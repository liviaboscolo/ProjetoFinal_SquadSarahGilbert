from django.shortcuts import render, get_object_or_404
from usuarios.forms import cadastro_forms
from .models import CustomUser


def cadastro_pessoa(request):
 form = cadastro_forms()
 pessoas = CustomUser.objects.all()
 return render(request, 'cadastro_pessoa.html',{'form': form})