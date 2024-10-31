from django.contrib import admin
from animais.models import Animal, Adocao, RegistroMedico

# Register your models here.
admin.site.register(Animal)
admin.site.register(Adocao)
admin.site.register(RegistroMedico)