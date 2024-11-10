from django.db import models
from django.core.validators import MinValueValidator

class Plataforma(models.Model):
    TIPOS = [
        ('Consola', 'Consola'),
        ('PC', 'PC'),
        ('Movil', 'Movil')
    ]

    tipo = models.CharField(max_length=200, choices=TIPOS)
    generacion = models.CharField(max_length=200)
    almacenamiento = models.IntegerField()
    fabricante = models.CharField(max_length=200)
    precio = models.FloatField(max_length=50)
    
def __str__(self):
        return Plataforma

class Juego(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)
    fecha_lanz = models.DateField()
    desarrolladora = models.CharField(max_length=100)
    precio = models.FloatField(validators=[MinValueValidator(0)])

def __str__(self):
        return Juego

class Genero(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)
    dificultad = models.CharField(max_length=100)
    tematica = models.CharField(max_length=100)
    formato = models.CharField(max_length=20, choices=[('MULTIJUGADOR', 'Multijugador'), ('SOLO', 'Solo')])

def __str__(self):
        return Genero