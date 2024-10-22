from django.urls import path 
from .import views 

urlpatterns = [
    path('',views.home,name='home'),
    path('detalhes/<int:id>/', views.detalhes, name='detalhes'),
]