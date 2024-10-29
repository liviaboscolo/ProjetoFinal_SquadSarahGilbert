from django.urls import path 
from . import views 

urlpatterns = [
    #path('',views.cadastro_pessoa,name='cadastro_pessoa'),
    path('minhas-solicitacoes', views.minhas_solicitacoes, name='minhas_solicitacoes'),
    path('cadastro-pessoa', views.cadastro_pessoa, name='cadastro_pessoa'),
    path('logout', views.logout_view, name='logout'),
    path('login/', views.user_login, name='login'),
    
]