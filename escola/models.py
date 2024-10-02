from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Professor(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    nome = models.CharField(max_length=150, null=False, blank=False)
    nascimento = models.DateField(null=False, blank=False)
    sexo = models.CharField(max_length=20, choices={'M': 'Masculino', 'F': 'Feminino', 'O': 'Outro'}, null=False, blank=False)
    cep = models.CharField(max_length=8, null=False, blank=False)
    pais = models.CharField(max_length=50, null=False, blank=False)
    bairro = models.CharField(max_length=250, null=True, blank=True)
    cidade = models.CharField(max_length=50, null=False, blank=False)
    estado = models.CharField(max_length=50, null=False, blank=False)
    logradouro = models.CharField(max_length=255, null=False, blank=False)
    numero = models.CharField(max_length=10, null=True, blank=True)
    endereco = models.CharField(max_length=255, null=False, blank=False)
    cpf = models.CharField(max_length=11, null=False, blank=False)