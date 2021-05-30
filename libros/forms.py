from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    """ Formulario para añadir libros """

    class Meta:
        model = Libro 

        fields = ['portada', 'titulo', 'autor', 'categorias']

        widgets = {
            'portada': forms.FileInput(attrs={'class':'form-control', 'placeholder': 'Portada'}),
            'titulo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título del libro'}),
            'autor': forms.Select(attrs={'class':'form-control'}),
            'categorias': forms.SelectMultiple(attrs={'class':'form-control'})
        }

        labels = {
            'titulo':'Título', 'autor': 'Autor', 'categorias':'Categorías (ctrl+click Multiopción)', 'portada': 'Portada'
        }