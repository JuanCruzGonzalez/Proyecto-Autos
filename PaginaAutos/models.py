from django.db import models

# Create your models here.
class Auto(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    motor = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="autos", null=True, blank=True)
    def __str__(self) -> str:
        return f"{self.nombre} {self.marca} | Motor: {self.motor} | Modelo: {self.modelo} | Marca: {self.marca} | Imagen: {self.imagen}"

