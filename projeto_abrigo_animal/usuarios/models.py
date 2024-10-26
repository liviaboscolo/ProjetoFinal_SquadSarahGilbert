from django.db import models
from django.contrib.auth.models import AbstractUser

TIPO_USER =(
    ('voluntarios', 'voluntarios'),
    ('usuario', 'usuario'),
    ('cuidador', 'cuidador'),

    
)

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField()
    senha = models.CharField(max_length=15)
    permissao = models.CharField(max_length= 20,choices=TIPO_USER,default="usuario")
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        
        def __str__(self):
         return self.nome
    