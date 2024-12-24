from django.db import models

# Create your models here.
class Categoria(models.Model):
    titulo = models.CharField(max_length=128)
    descripcion = models.CharField(max_length=256)

class Pelicula(models.Model):
    titulo = models.CharField(max_length=128)
    descripcion = models.CharField(max_length=256)
    lanzamiento = models.DateField()
    categoria = models.ForeignKey(Categoria, 
                                  on_delete=models.PROTECT)
