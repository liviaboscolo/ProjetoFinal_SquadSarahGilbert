from django.contrib import admin
from .models import CustomUser, Voluntario, Cuidador


# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Voluntario)
admin.site.register(Cuidador)

