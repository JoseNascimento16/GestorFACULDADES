# Generated by Django 4.1.6 on 2023-02-05 02:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
        ('professores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='curso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cursos.curso'),
        ),
    ]
