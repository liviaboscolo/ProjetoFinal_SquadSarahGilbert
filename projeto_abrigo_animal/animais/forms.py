from django import forms
SEXO_CHOICES =(
    ('M', 'Macho'),
    ('F', 'Femea'), 
)
TIPO_CHOICES =(
    ('Cao', 'Cachorro'),
    ('Gato', 'Gato'),
)

class AnimalForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=30)
    sexo = forms.ChoiceField(label='Sexo', choices=SEXO_CHOICES)
    idade = forms.IntegerField()
    cor =forms.CharField(label='Cor', max_length= 25)
    tipo = forms.ChoiceField(label='Tipo', choices = TIPO_CHOICES)
    raca = forms.CharField(label='Raça', max_length= 30)
    foto_upload = forms.FileField(label='Foto Upload')