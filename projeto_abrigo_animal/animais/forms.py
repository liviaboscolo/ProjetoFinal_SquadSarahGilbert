from django import forms
from .models import Animal, Adocao

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'
        
class AdocaoForm(forms.ModelForm):
    class Meta:
        model = Adocao
        fields = ['tipo_residencia', 'telado']
        