from django.db import models
from django.contrib.auth.models import User

class Empresa(models.Model):
    razao_social = models.CharField(max_length=100)
    email = models.EmailField()
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    ramo_empresa = models.CharField(max_length=100)

    def __str__(self):
        return self.razao_social

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20, blank=True)
    cpf = models.CharField(max_length=14, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.username