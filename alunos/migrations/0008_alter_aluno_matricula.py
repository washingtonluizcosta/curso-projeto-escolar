# Generated by Django 5.0.6 on 2024-10-02 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0007_aluno_matricula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='matricula',
            field=models.CharField(blank=True, max_length=6),
        ),
    ]
