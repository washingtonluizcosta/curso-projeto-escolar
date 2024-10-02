from django.db import models

class Disciplina(models.Model):
    nome = models.CharField(max_length=150, null=False, blank=False)
    carga_horaria = models.IntegerField(null=False, blank=False)

class Turma(models.Model):
    horario = models.TimeField(null=False, blank=False)
    turno = models.CharField (max_length=10, choices={'Manha': 'Manha', 'Tarde': 'Tarde', 'Noite': 'Noite'}, null=False, blank=False)
    data_inicio = models.DateField(null=False, blank=False)
    data_conclusao = models.DateField(null=False, blank=False)