from django import forms
from Aplicacion.models import Juego, Plataforma, Genero

class FormJuego(forms.ModelForm):
    class Meta:
        model = Juego
        fields = 'all'

class FormPlataforma(forms.ModelForm):
    class Meta:
        model = Plataforma
        fields = 'all'

class FormGenero(forms.ModelForm):
    class Meta:
        model = Genero
        fields = 'all'