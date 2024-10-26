from django.urls import path 
from .import views 

urlpatterns = [
    #path('',views.cadastro_pessoa,name='cadastro_pessoa'),
    path('cadastro_pessoa', views.cadastro_pessoa, name='cadastro_pessoa'),
    
]