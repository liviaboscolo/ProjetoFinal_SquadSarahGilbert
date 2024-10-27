from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
# Create your models here.

TIPO_USER =(
    ('administrador', 'Administrador'),
    ('usuario', 'Usuario'),
    ('cuidador', 'cuidador'),
    ('voluntario', 'Voluntario'),
    
)

class CustomUser(AbstractUser):
    estado = models.CharField(max_length=15)
    cidade = models.CharField(max_length=15)
    ##permissao = models.CharField(max_length= 20,choices=TIPO_USER,default="usuario")
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        
        def __str__(self):
         return self.nome
    
