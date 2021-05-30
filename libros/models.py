from django.db import models
from core.models import Categoria, Autor

class Libro(models.Model):
    """ Modelo de libros """

    titulo = models.CharField(max_length=200, verbose_name="Título")
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, verbose_name="Autor")
    categorias = models.ManyToManyField(Categoria, verbose_name="Categorías")
    portada = models.ImageField(upload_to="media/portadas/", verbose_name="Portada", blank=True, null=True)

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Listado de Libros"
        ordering = ["titulo"]

    def __str__(self):
        return self.titulo