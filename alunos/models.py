from django.db import models
from django.contrib.auth.models import User
import random


# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=150, null=False, blank=False)
    nascimento = models.DateField(null=False, blank=False)
    sobre = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    sexo = models.CharField(max_length=20, choices={'M': 'Masculino', 'F': 'Feminino', 'O': 'Outro'}, null=False, blank=False)
    cep = models.CharField(max_length=8, null=False, blank=False)
    pais = models.CharField(max_length=50, null=False, blank=False)
    bairro = models.CharField(max_length=250, null=True, blank=True)
    cidade = models.CharField(max_length=50, null=False, blank=False)
    estado = models.CharField(max_length=50, null=False, blank=False)
    logradouro = models.CharField(max_length=255, null=False, blank=False)
    numero = models.CharField(max_length=10, null=True, blank=True)
    endereco = models.CharField(max_length=255, null=False, blank=False)
    nome_mae = models.CharField(max_length=150, null=True, blank=True)
    nome_pai = models.CharField(max_length=150, null=True, blank=True)
    cpf = models.CharField(max_length=11, null=False, blank=False)
    matricula = models.CharField(max_length=6)
    sobre = models.TextField(null=True)
    email = models.EmailField()

    def save(self, *args, **kwargs):
        self.matricula = self.codigo_matricula()
        super(Aluno, self).save(*args, **kwargs)

    def codigo_matricula(self):
        codigo = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
                  '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        c1 = random.choice(codigo)
        c2 = random.choice(codigo)
        c3 = random.choice(codigo)
        c4 = random.choice(codigo)
        c5 = random.choice(codigo)
        c6 = random.choice(codigo)
        return f'{c1}{c2}{c3}{c4}{c5}{c6}'