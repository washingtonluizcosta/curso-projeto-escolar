from django.db import models
from django.contrib.auth.models import User
import random


# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=150, null=False, blank=False)
    nascimento = models.DateField(null=False, blank=False)
    sobre = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    sexo = models.CharField(max_length=1, choices={'M': 'Masculino', 'F': 'Feminino', 'O': 'Outro'}, null=False, blank=False)
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
    cpf = models.CharField(max_length=11, unique=True, null=False, blank=False)
    matricula = models.CharField(max_length=6) 
    sobre = models.TextField(null=True)
    email = models.EmailField()

    def definir_matricula(self, matricula):
        letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
        numero1 = random.randrange(0,9)
        numero2 = random.randrange(0,9)
        numero3 = random.randrange(0,9)
        letra1 = random.choice(letras)
        letra2 = random.choice(letras)
        letra3 = random.choice(letras)
        matricula = f'{numero1} + {numero2} + {numero3} + {letra1}+ {letra2} + {letra3}'
        self.matricula = matricula

        
