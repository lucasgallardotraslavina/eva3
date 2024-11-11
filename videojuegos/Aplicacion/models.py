from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models

def validate_positive(value):
    if value < 0:
        raise ValidationError(f"El valor {value} no puede ser negativo. Por favor ingresa un valor positivo.")

class Plataforma(models.Model):
    TIPOS = [
        ('Consola', 'Consola'),
        ('PC', 'PC'),
        ('Movil', 'Movil')
    ]

    tipo = models.CharField(max_length=200, choices=TIPOS)
    generacion = models.CharField(max_length=200)
    almacenamiento = models.IntegerField(validators=[validate_positive])
    fabricante = models.CharField(max_length=200)
    precio = models.FloatField(validators=[MinValueValidator(0), validate_positive])

    def __str__(self):
        return f"{self.tipo} - {self.fabricante}"

class Genero(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)
    dificultad = models.CharField(max_length=100)
    tematica = models.CharField(max_length=100)
    formato = models.CharField(max_length=20, choices=[('MULTIJUGADOR', 'Multijugador'), ('SOLO', 'Solo')])

    def __str__(self):
        return self.nombre

class Juego(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)
    fecha_lanz = models.DateField()
    desarrolladora = models.CharField(max_length=100)
    precio = models.FloatField(validators=[MinValueValidator(0)])
    

    generos = models.ManyToManyField(Genero, related_name="juegos")
    plataforma = models.ForeignKey(Plataforma, on_delete=models.CASCADE, related_name="juegos", null=True, blank=True)

    def __str__(self):
        return self.nombre
