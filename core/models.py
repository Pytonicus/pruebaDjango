from django.db import models

class Categoria(models.Model):
    """ Listado de categorías """

    nombre = models.CharField(max_length=200, verbose_name="Nombre Categoría")

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre

class Autor(models.Model):
    """ Lista de autores """

    nombre = models.CharField(max_length=200, verbose_name="Autor")
    fecha_nacimiento = models.DateField(verbose_name="Fecha de nacimiento", blank=True, null=True)
    foto = models.ImageField(upload_to="media/fotos/", blank=True, null=True)

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre