# Generated by Django 3.2 on 2024-11-11 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion', '0004_auto_20241110_1431'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='juego',
            name='generos',
        ),
    ]
