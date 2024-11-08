from django.db import models
from django.core.validators import MinValueValidator

class Plataforma(models.Model):
    TIPOS = [
        ('Consola', 'Consola'),
        ('PC', 'PC'),
        ('Movil', 'Movil')
    ]

    tipo = models.CharField(max_length=20, choices=TIPOS)
    generacion = models.CharField(max_length=20)
    almacenamiento = models.IntegerField()
    fabricante = models.CharField(max_length=20)
    precio = models.FloatField()

class Juego(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)
    fecha_lanz = models.DateField()
    desarrolladora = models.CharField(max_length=100)
    precio = models.FloatField(validators=[MinValueValidator(0)])

class Genero(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)
    dificultad = models.CharField(max_length=30)
    tematica = models.CharField(max_length=100)
    formato = models.CharField(max_length=50)
