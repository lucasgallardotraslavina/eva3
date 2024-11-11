# forms.py

from django import forms
from Aplicacion.models import Juego, Plataforma, Genero

class FormJuego(forms.ModelForm):
    generos = forms.ModelMultipleChoiceField(
        queryset=Genero.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    
    class Meta:
        model = Juego
        fields = '__all__'

class FormPlataforma(forms.ModelForm):
    class Meta:
        model = Plataforma
        fields = '__all__'

class FormGenero(forms.ModelForm):
    class Meta:
        model = Genero
        fields = '__all__'
