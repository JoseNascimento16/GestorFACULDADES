# Generated by Django 4.1.6 on 2023-02-03 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('disciplinas', '0001_initial'),
        ('notas', '0003_alter_nota_nota'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='disciplina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='disciplinas.disciplina'),
        ),
    ]
