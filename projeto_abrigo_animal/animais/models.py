from django.db import models

# Create your models here.
#	Nome, idade, cor, tipo, raça, foto


class Animal(models.Model):
    nome = models.CharField(max_length=30)
    idade = models.IntegerField()
    cor = models.CharField(max_length=10)
    tipo = models.CharField(max_length=20)
   # foto =models.ImageField()