# Generated by Django 3.2 on 2024-11-09 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion', '0002_auto_20241108_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genero',
            name='dificultad',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='plataforma',
            name='fabricante',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='plataforma',
            name='generacion',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='plataforma',
            name='precio',
            field=models.FloatField(max_length=50),
        ),
        migrations.AlterField(
            model_name='plataforma',
            name='tipo',
            field=models.CharField(choices=[('Consola', 'Consola'), ('PC', 'PC'), ('Movil', 'Movil')], max_length=200),
        ),
    ]
