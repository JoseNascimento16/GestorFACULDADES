# Generated by Django 4.1.6 on 2023-02-05 02:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0003_aluno_curso'),
        ('disciplinas', '0001_initial'),
        ('notas', '0004_alter_nota_disciplina'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='aluno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='alunos.aluno'),
        ),
        migrations.AlterField(
            model_name='nota',
            name='disciplina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disciplinas.disciplina'),
        ),
    ]
