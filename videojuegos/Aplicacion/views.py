from django.shortcuts import render,redirect
from Aplicacion.models import Plataforma, Juego, Genero
from Aplicacion.forms import FormPlataforma , FormJuego, FormGenero
# Create your views here.

def index(request):
    return render(request, 'Aplicacion/index.html')

def listadoPlataforma(request):
    plataformas = Plataforma.objects.all()
    data = {'plataformas': plataformas}
    return render(request, 'Aplicacion/Plataformas.html', data)

def agregarPlataforma(request):
    form = FormPlataforma()
    if request.method == 'POST':
        form = FormPlataforma(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request,'Aplicacion/agregarPlataformas.html', data)

def eliminarPlataforma(requuest,id):
    plataforma = Plataforma.objects.get(id = id)
    plataforma.delete()
    return redirect('../plataformas/')

def actualizarPlataforma(request, id):
    plataforma = Plataforma.objects.get(id = id)
    form = FormPlataforma(instance = plataforma)
    if request.method == 'POST':
        form = FormPlataforma(request.POST, instance = plataforma)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render(request,'Aplicacion/agregarPlataformas.html', data)

#==================================================================
def index(request):
    return render(request,'Aplicacion/index.html')

def listadoJuegos(request):
    juegos = Juego.objects.all()
    data = {'juegos' : juegos}
    return render(request, 'Aplicacion/juegos.html',data)

def agregarJuego(request):
    form = FormJuego()
    if request.method == 'POST':
        form = FormJuego(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'Aplicacion/agregarJuego.html',data)

def eliminarJuego(request, id):
    juego = Juego.objects.get(id = id)
    juego.delete()
    return redirect('/juegos/')

def actualizarJuego(request, id):
    juego = Juego.objects.get(id = id)
    form = FormJuego(instance=juego)
    if request.method == 'POST':
        form = FormJuego(request.POST, instance=juego)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render (request, 'Aplicacion/agregarJuego.html',data)

#================================================================
def listadoGenero(request):
    generos = Genero.objects.all()
    data = {'generos': generos}
    return render(request, 'Aplicacion/generos.html', data)

def agregarGenero(request):
    form = FormGenero()
    if request.method == 'POST':
        form = FormGenero(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request,'Aplicacion/agregarGenero.html', data)

def eliminarGenero(request,id):
    genero = Genero.objects.get(id = id)
    genero.delete()
    return redirect('../generos/')

def actualizarGenero(request, id):
    genero = Genero.objects.get(id = id)
    form = FormGenero(instance = genero)
    if request.method == 'POST':
        form = FormGenero(request.POST, instance = genero)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render(request,'Aplicacion/agregarGenero.html', data)
