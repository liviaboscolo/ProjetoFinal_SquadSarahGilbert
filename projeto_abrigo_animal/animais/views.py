from django.shortcuts import render, get_object_or_404
from animais.forms import AnimalForm
from .models import Animal
# Create your views here.
def home(request):
    form = AnimalForm()  # Cria uma instância do formulário
    animais = Animal.objects.all()  # Recupera todos os animais do banco de dados
    return render(request, 'home.html', {'animais': animais, 'form': form})

def detalhes(request, id):
    animal = get_object_or_404(Animal, id=id)  # Ou use outro campo único
    return render(request, 'detalhes.html', {'animal': animal})


from django.shortcuts import render, get_object_or_404
from animais.forms import AnimalForm
from .models import Animal
#from PIL import Image
from django.http import HttpResponse
from django.conf import settings
import os
from django.http import HttpResponseRedirect

# Create your views here.
def cadastro_animal(request):
     if request.method == 'POST':
      form = AnimalForm(request.POST, request.FILES)  # Cria uma instância do formulário 
      if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
     else :
        form = AnimalForm()  # Cria uma instância do formulário
        return render(request, 'cadastro_animal.html',{'form': form})
    