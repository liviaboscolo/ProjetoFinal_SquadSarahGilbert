from django import forms
from .models import Animal, Adocao, RegistroMedico

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'
        
class AdocaoForm(forms.ModelForm):
    class Meta:
        model = Adocao
        fields = ['tipo_residencia', 'telado']

DETALHES_MEDICOS_CHOICES = [
        ('VACINADO', 'Vacinado'),
        ('VERMIFUGADO', 'Vermifugado'),
        ('CASTRADO', 'Castrado'),
    ]
class CombinedForm(forms.ModelForm):
    # Include Cuidados fields
    veterinario = forms.CharField(max_length=50)
    detalhes_medicos = forms.MultipleChoiceField(
        choices=DETALHES_MEDICOS_CHOICES,
        widget=forms.CheckboxSelectMultiple,  # or forms.SelectMultiple for a dropdown
        label="Detalhes Médicos"
    )

    class Meta:
        model = Animal
        fields = '__all__'  # Include all fields from Animal model
        exclude = ['status','descricao']
        widgets = {
            'estado': forms.TextInput(attrs={'placeholder': 'SP'}),
            'cidade': forms.TextInput(attrs={'placeholder': 'São Paulo'})
        }

    def save(self, user, commit=True):
        # Save the Animal instance
        animal_instance = super().save(commit=commit)

        # Save the Cuidados instance
        if commit:
            # Create the Cuidados instance using the combined form data
            RegistroMedico.objects.create(
                animal=animal_instance,
                user=user,  # Make sure to set the user from your view
                veterinario=self.cleaned_data['veterinario'],
                detalhes_medicos=self.cleaned_data['detalhes_medicos']
            )

        return animal_instance