from django.shortcuts import render
from .models import Libro, Categoria
from .forms import LibroForm

def home(request, categoria = None):
    """ Página principal que lista los libros """

    try:
        clave = Categoria.objects.get(nombre=categoria)
        libros = Libro.objects.filter(categorias=clave)
    except:
        libros = Libro.objects.all()

    categorias = Categoria.objects.all()

    form = LibroForm()

    return render(request, 'libros.html', {
        'libros':libros, 
        'categorias':categorias,
        'categoria':categoria,
        'form': form
        })
