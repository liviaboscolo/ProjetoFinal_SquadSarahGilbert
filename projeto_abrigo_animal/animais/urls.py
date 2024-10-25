from django.urls import path 
from .import views 

urlpatterns = [
    path('',views.home,name='home'),
    path('detalhes/<int:id>/', views.detalhes, name='detalhes'),
    path('cadastro_animal',views.cadastro_animal ,name= 'cadastro_animal'),
    path('map/', views.map_view, name='map'),
    
]