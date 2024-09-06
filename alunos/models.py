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
    matricula = models.CharField(max_length=6, blank=True)
    sobre = models.TextField(null=True)
    email = models.EmailField()

   def save(self, *args, **kwargs):
        if not self.matricula:
            codigo = self.codigo_matricula()
            while Aluno.objects.filter(matricula = codigo).exists():
                codigo = self.codigo_matricula()    
            self.matricula = codigo
        super(Aluno, self).save(*args, **kwargs)

    def codigo_matricula(self):
        letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        codigo = []
        codigo.append(random.choice(letras))
        codigo.append(random.choice(letras))
        codigo.append(random.choice(letras))
        codigo.append(random.randrange(0, 10))
        codigo.append(random.randrange(0, 10))
        codigo.append(random.randrange(0, 10))
        random.shuffle(codigo)
        return f'{codigo[0]}{codigo[1]}{codigo[2]}{codigo[3]}{codigo[4]}{codigo[5]}'
