from django.contrib import admin
from .models import CustomUser, Voluntario, Cuidador


# Register your models here.
admin.register(CustomUser)
admin.register(Voluntario)
admin.register(Cuidador)

