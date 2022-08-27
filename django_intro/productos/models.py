from django.db import models

# Create your models here.
class Productos(models.Model):
    productoId = models.AutoField(primary_key=True)
    productoNombre = models.CharField(max_length=255)
    productoDescripcion = models.CharField(max_length=255)
    productoPrecio = models.FloatField(default=0.00)
    estado = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.productoNombre