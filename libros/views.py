from django.shortcuts import render, redirect
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

    if request.method == "POST":
        try:
            if request.POST["edicion"] == "1":
                libro = Libro.objects.get(id=request.POST["id"])
                form = LibroForm(request.POST, request.FILES, instance=libro)

                if form.is_valid():
                    # recibir y convertir en diccionario el post:
                    r = dict(request.POST)
                    # Ahora si recupera múltiples selecciones en lugar de una:
                    cat = r["categorias"]
                    libro.save()
                    libro.categorias.set(cat)
                    return redirect('home')
                else:
                    form = LibroForm()
        except:
            form = LibroForm(request.POST, request.FILES)

            if form.is_valid():
                registro = form.save()
                return redirect('home')
            else:
                form = LibroForm()



    return render(request, 'libros.html', {
        'libros':libros, 
        'categorias':categorias,
        'categoria':categoria,
        'form': form
        })

def borrar_libro(request, libro):
    """ Borra un libro """

    Libro.objects.filter(id=libro).delete()
    return redirect('home')