from django.urls import path 
from .import views 

urlpatterns = [
    path('',views.cadastro_pessoa,name='cadastro_pessoa'),
    #path('detalhes/<int:id>/', views.detalhes, name='detalhes'),
    
]