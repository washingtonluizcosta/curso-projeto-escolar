# Generated by Django 5.0.7 on 2024-09-02 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0006_alter_aluno_sexo'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='matricula',
            field=models.CharField(default='abc123', max_length=6),
            preserve_default=False,
        ),
    ]
