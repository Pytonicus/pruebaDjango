from django.contrib import admin
from django.utils.html import format_html
from .models import Categoria, Autor

class AutorAdmin(admin.ModelAdmin):
    """ Configurar comportamiento de listado admin """

    list_display = ('fotografia', 'nombre', 'fecha_nacimiento')

    def fotografia(self, obj):
        try:
            result = format_html("<img src={} height='75' />", obj.foto.url)
        except:
            result = format_html("<img src={} height='75' />", "/static/img/no-foto.jpg")
        return result

admin.site.register(Categoria)
admin.site.register(Autor, AutorAdmin)