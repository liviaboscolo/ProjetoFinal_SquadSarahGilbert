from django.shortcuts import render
from animais.forms import AnimalForm
# Create your views here.
def home(request):
    form = AnimalForm()
    return render(request, 'home.html',{'form':form})