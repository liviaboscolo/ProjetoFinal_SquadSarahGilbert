from django.db import models
from multiselectfield import MultiSelectField


class Animal(models.Model):
    DETALHES_MEDICOS_CHOICES = [
        ('VACINADO', 'Vacinado'),
        ('VERMIFUGADO', 'Vermifugado'),
        ('CASTRADO', 'Castrado'),
    ]
    
    nome = models.CharField(max_length=30)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=10, choices=[('Macho', 'Macho'), ('Fêmea', 'Fêmea')], default='Desconhecido')
    cor = models.CharField(max_length=10)
    tipo = models.CharField(max_length=20)
    raca = models.CharField(max_length=20, default='SRD')
    porte = models.CharField(max_length=10, choices=[('PEQUENO', 'Pequeno'), ('MÉDIO', 'Médio'), ('GRANDE', 'Grande')], default='Desconhecido')
    detalhes_medicos = MultiSelectField(choices=DETALHES_MEDICOS_CHOICES, max_length=50)
    descricao = models.TextField(blank=True)  # O campo pode ser deixado em branco

    def save(self, *args, **kwargs):
        # Preencher a descrição com base nos outros campos
        self.descricao = f"{self.nome}, com {self.idade} anos e tamanho {self.porte}. Adora crianças e ama brincar ❤️. Está à procura de uma nova família. Ajude a encontrar um lar amoroso!"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome
