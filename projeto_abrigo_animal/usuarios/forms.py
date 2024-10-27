from django import forms
from .models import CustomUser

class CadastroForm(forms.ModelForm):
    
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
    

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=100, 
        required=True, 
        widget=forms.TextInput(attrs={'placeholder': 'Seu usuário', 'class': 'form-control'}),
        label= 'Usuário'
    )
    password = forms.CharField(
        required=True, 
        widget=forms.PasswordInput(attrs={'placeholder': 'Sua senha', 'class': 'form-control'}),
        label= 'Senha'
    )






