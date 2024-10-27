from django import forms
from .models import CustomUser

class cadastro_forms(forms.ModelForm):
    
    class Meta:
        model = CustomUser
        fields = ['username','first_name','last_name','cidade','estado','email','password'] #'__all__'
        labels = {
            'email': 'Email'
        }
        widgets = {
            'password': forms.PasswordInput(),  # Aqui você define o widget para o campo de senha
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True  # Torna todos os campos obrigatórios

    def save(self, commit=True):
        user = super().save(commit=False)  # Cria o objeto, mas não salva no banco ainda
        user.set_password(self.cleaned_data['password'])  # Criptografa a senha
        if commit:
            user.save()  # Salva o objeto no banco de dados
        return user
    

class login(forms.Form):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True  # Torna todos os campos obrigatórios

    def save(self, commit=True):
        user = super().save(commit=False)  # Cria o objeto, mas não salva no banco ainda
        user.set_password(self.cleaned_data['password'])  # Criptografa a senha
        if commit:
            user.save()  # Salva o objeto no banco de dados
        return user



