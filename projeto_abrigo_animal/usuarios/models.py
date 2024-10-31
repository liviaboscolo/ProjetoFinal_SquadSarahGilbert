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

class Voluntario(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Referência ao modelo User
    status = models.CharField(max_length=100, choices=[('analise', 'Análise'), ('aprovado', 'Aprovado'),('reprovado','Reprovado')], default='analise')
    experiencia = models.CharField(max_length=50, choices=[('sim', 'Sim'), ('nao', 'Não')])
    descricao = models.TextField(blank=False)

    def __str__(self):
        return f'{self.user}'

class Cuidador(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Referência ao modelo User
    status = models.CharField(max_length=100, choices=[('analise', 'Análise'), ('aprovado', 'Aprovado'),('reprovado','Reprovado')], default='analise')
    experiencia = models.CharField(max_length=50, choices=[('sim', 'Sim'), ('nao', 'Não')])
    formacao = models.CharField(max_length=100)
    descricao = models.TextField(blank=False)
    
    class Meta:
        verbose_name = 'Cuidador'
        verbose_name_plural = 'Cuidadores'

    def __str__(self):
        return f'{self.user}'
