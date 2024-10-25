from django.db import models
from django.core.files.storage import FileSystemStorage
from multiselectfield import MultiSelectField

DETALHES_MEDICOS_CHOICES = [
        ('VACINADO', 'Vacinado'),
        ('VERMIFUGADO', 'Vermifugado'),
        ('CASTRADO', 'Castrado'),
    ]
TIPO_CHOICES =(
    ('Cao', 'Cachorro'),
    ('Gato', 'Gato'),
)
fs = FileSystemStorage(location='media/images')
class Animal(models.Model):
    status = models.CharField(max_length=10, choices=[('Dispobivel', 'disponivel'), ('Adotado', 'adotado')], default='Desconhecido')
    nome = models.CharField(max_length=30)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=10, choices=[('Macho', 'Macho'), ('Fêmea', 'Fêmea')], default='Desconhecido')
    cor = models.CharField(max_length=10)
    tipo = models.CharField(max_length=10 ,choices=TIPO_CHOICES)
    raca = models.CharField(max_length=20, default='SRD')
    porte = models.CharField(max_length=10, choices=[('PEQUENO', 'Pequeno'), ('MÉDIO', 'Médio'), ('GRANDE', 'Grande')], default='Desconhecido')
    detalhes_medicos = MultiSelectField(choices=DETALHES_MEDICOS_CHOICES, max_length=50)
    descricao = models.TextField(blank=True)  # O campo pode ser deixado em branco
    foto_animal = models.ImageField(upload_to='images/', storage=fs, blank=True)   # Armazena as imagens na pasta media/images

    def save(self, *args, **kwargs):
        # Preencher a descrição com base nos outros campos
        self.descricao = f"{self.nome}, com {self.idade} anos e tamanho {self.porte}. Adora crianças e ama brincar ❤️. Está à procura de uma nova família. Ajude a encontrar um lar amoroso!"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome
