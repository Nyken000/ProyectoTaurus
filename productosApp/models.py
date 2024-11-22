from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    imagen = models.CharField(max_length=255, blank=True, null=True)  # Ruta relativa a static/img/

    def __str__(self):
        return self.nombre
