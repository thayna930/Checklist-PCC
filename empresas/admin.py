from django.contrib import admin
from .models import Empresa
from empresas import models

admin.site.register(Empresa)

@admin.register(models.UserProfile)
class UserProfile(admin.ModelAdmin):
    list_display = 'user_id', 'cidade', 'estado', 'telefone', 'cpf','data_nascimento', 'id',