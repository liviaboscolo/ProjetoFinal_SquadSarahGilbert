from django.shortcuts import render, get_object_or_404
from animais.forms import AnimalForm,AdocaoForm
from .models import Animal
#from PIL import Image
from django.http import HttpResponse
from django.conf import settings
import os
from django.http import HttpResponseRedirect
import folium
import requests
from django.contrib.auth.decorators import login_required

# ----------------------------------------------------------------------- HOME

def home(request):
    form = AnimalForm()  # Cria uma instância do formulário
    animais = Animal.objects.all()  # Recupera todos os animais do banco de dados

    if request.method == "GET":
        nome_pet = request.GET.get('nome_pet')
        especie = request.GET.get('especie')  # O ID da espécie não é mais necessário
        genero = request.GET.get('genero')
        porte = request.GET.get('porte')
        estado = request.GET.get('estado')
        cidade = request.GET.get('cidade')

        # Filtrando os animais com base nos critérios fornecidos
        if nome_pet:
            animais = animais.filter(nome__icontains=nome_pet)
        if especie:  # Assumindo que 'especie' é uma string correspondente a 'tipo'
            animais = animais.filter(tipo=especie)
        if genero:
            animais = animais.filter(sexo=genero)
        if porte:
            animais = animais.filter(porte=porte)
        if estado:
            animais = animais.filter(estado=estado)
        if cidade:
            animais = animais.filter(cidade=cidade)

    return render(request, 'home.html', {'animais': animais, 'form': form})




# ----------------------------------------------------------------------- MAP

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
import ipaddress

def get_client_ipv4(request):
    ip = get_client_ip(request)
    
    # Validate if it's an IPv4 address
    try:
        ip_obj = ipaddress.ip_address(ip)
        if isinstance(ip_obj, ipaddress.IPv4Address):
            return str(ip_obj)  # Return only IPv4 address as a string
        else:
            return None  # If it's an IPv6, return None or handle it differently
    except ValueError:
        return None  # In case the IP is invalid or not parsable

def get_geolocation(ip_address):
    #ip_address = 'your_ip_address'  # Use 'your_ip_address' or 'check' for your current IP
    url = f'http://ip-api.com/json/{ip_address}'

    response = requests.get(url)
    data = response.json()

    print(data)

    latitude = data['lat']
    longitude = data['lon']

    return latitude, longitude

def map_view(request, lat=-23.9613 ,lon=-46.391):
    mapa = folium.Map(location=[-22.449, -48.6388], zoom_start=6.5) # location starter
    folium.Marker(location=[-21.1775000, -47], icon=folium.Icon(popup="Star Icon",color='purple')).add_to(mapa)
    folium.Marker(location=[float(lat), float(lon)], icon=folium.Icon(color='orange')).add_to(mapa)
    mapa.save('animais/templates/map.html')
    return render(request, 'map.html')

# ----------------------------------------------------------------------- DETALHES

#@login_required
def detalhes(request, id): # 
    print(request)
    ip = get_client_ip(request)
    ip = '177.100.236.65'
    lat, lon = get_geolocation(ip)

    animal = get_object_or_404(Animal, id=id)  # Ou use outro campo único
    animais = Animal.objects.all()  # Recupera todos os animais para a galeria
    map_view(request, lat, lon)
    return render(request, 'detalhes.html', {'animal': animal, 'animais': animais})





# ----------------------------------------------------------------------- CADASTRO ANIMAL

#@login_required
def cadastro_animal(request):
     if request.method == 'POST':
      form = AnimalForm(request.POST, request.FILES)  # Cria uma instância do formulário 
      if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
     else :
        form = AnimalForm()  # Cria uma instância do formulário
        return render(request, 'cadastro_animal.html',{'form': form})
     
# ----------------------------------------------------------------------- CADASTRO ANIMAL

def solicitacao_adocao(request, id):
    animal = get_object_or_404(Animal, id=id)  # Obtém o animal pelo ID

    if request.method == 'POST':
        form = AdocaoForm(request.POST, request.FILES)
        if form.is_valid():
            adocao = form.save(commit=False)  # Não salva ainda
            adocao.animal = animal  # Associa o animal à adoção
            adocao.user = request.user  # Associa o usuário à adoção
            adocao.save()  # Agora salva
    else:
        form = AdocaoForm()

    return render(request, 'solicitacao_adocao.html', {'form': form, 'animal': animal})
     

# ----------------------------------------------------------------------- LIVIA


def quero_ajudar(request):
    return render(request, 'quero_ajudar.html')
     
def sobre_nos(request):
    return render(request, 'sobre_nos.html')


