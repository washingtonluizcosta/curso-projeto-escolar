from django.db import models

# Create your models here.
# alunos_aluno
class Aluno(models.Model):
    nome = models.CharField(max_length=150, null=False, blank=False)
    nascimento = models.DateField(null=False, blank=False)
    sobre = models.TextField(null=True)