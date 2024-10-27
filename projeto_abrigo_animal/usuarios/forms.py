from django import forms
from .models import CustomUser

class cadastro_forms(forms.ModelForm):
    
    class Meta:
        model = CustomUser
        fields = '__all__'