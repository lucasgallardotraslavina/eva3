from django.contrib import admin
from Aplicacion.models import Plataforma, Juego, Genero

# Register your models here.
class PlataformaAdmin(admin.ModelAdmin):
    list_display = ['tipo', 'generacion', 'almacenamiento', 'fabricante', 'precio']

class JuegoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'fecha_lanz', 'desarrolladora', 'precio']

class GeneroAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'dificultad', 'tematica', 'formato']

# Register your models here.
admin.site.register(Plataforma, PlataformaAdmin)
admin.site.register(Juego, JuegoAdmin)
admin.site.register(Genero, GeneroAdmin)
