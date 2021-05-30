from django.contrib import admin
from django.utils.html import format_html
from .models import Libro

class AdminLibro(admin.ModelAdmin):
    list_display = ('fotografia', 'titulo', 'autor', 'categorias_nombre')
    search_fields = ('titulo', 'autor__nombre', 'categorias__nombre')
    list_filter = ('autor__nombre', 'categorias__nombre')

    def fotografia(self, obj):
        try:
            result = format_html("<img src={} height='75' />", obj.portada.url)
        except:
            result = format_html("<img src={} height='75' />", "/static/img/sin-portada.jpg")
        return result

    def categorias_nombre(self, obj):
        return ", ".join([c.nombre for c in obj.categorias.all().order_by('nombre')])

    categorias_nombre.short_description = "Categoría"

admin.site.register(Libro, AdminLibro)