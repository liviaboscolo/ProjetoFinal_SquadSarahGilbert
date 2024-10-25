from django.urls import path 
from .import views 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home,name='home'),
    path('detalhes/<int:id>/', views.detalhes, name='detalhes'),
    path('cadastro_animal',views.cadastro_animal ,name= 'cadastro_animal'),
    path('map/', views.map_view, name='map'),
    
]

if settings.DEBUG:  # Isso é importante para garantir que a configuração de mídia só seja aplicada no modo de desenvolvimento
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)