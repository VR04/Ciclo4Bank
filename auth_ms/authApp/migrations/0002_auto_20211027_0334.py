# Generated by Django 3.2.7 on 2021-10-27 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='balance',
            new_name='creditosMateria',
        ),
        migrations.RemoveField(
            model_name='account',
            name='isActive',
        ),
        migrations.RemoveField(
            model_name='account',
            name='lastChangeDate',
        ),
        migrations.AddField(
            model_name='account',
            name='calificacionMateria',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='account',
            name='codigo',
            field=models.CharField(default='NoCodigo', max_length=30, verbose_name='Código'),
        ),
        migrations.AddField(
            model_name='account',
            name='nombreMateria',
            field=models.CharField(default='NoMateria', max_length=30, verbose_name='Nombre de la Materia'),
        ),
    ]
