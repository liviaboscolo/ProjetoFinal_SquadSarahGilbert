from django.urls import path 
from .import views 

urlpatterns = [
    #path('',views.cadastro_pessoa,name='cadastro_pessoa'),
    path('cadastro-pessoa', views.cadastro_pessoa, name='cadastro_pessoa'),
    
]