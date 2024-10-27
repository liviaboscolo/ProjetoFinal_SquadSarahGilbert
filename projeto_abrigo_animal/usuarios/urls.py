from django.urls import path 
from django.contrib import admin
from .import views 

urlpatterns = [
    #path('',views.cadastro_pessoa,name='cadastro_pessoa'),
    path('cadastro-pessoa', views.cadastro_pessoa, name='cadastro_pessoa'),
    path('login/', views.login, name='login'),
    
]