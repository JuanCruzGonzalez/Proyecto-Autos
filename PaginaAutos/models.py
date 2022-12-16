from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Auto(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    motor = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="autos", null=True, blank=True)
    def __str__(self) -> str:
        return f"{self.nombre} | Motor: {self.motor} | Modelo: {self.modelo} | Marca: {self.marca}"
        
class Mensaje(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mensaje=models.CharField(max_length=150)
    tiempo=models.TimeField(auto_now_add=True)
    def __str__(self) -> str:
        return f'{self.mensaje}'

class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    historia = models.CharField(max_length=100)
    fecha_creacion = models.DateField()
    pais = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.nombre} Creada el: {self.fecha_creacion.year} en {self.pais}. {self.historia} "


class AutoInstance(models.Model):
    ...
    class Meta:
        ...
        permissions = (("can_add_imagen_auto", "Agregar una imagen de auto"),("can_change_imagen_auto", "Cambiar una imagen de auto"), ("can_delete_imagen_auto", "Borrar una imagen de auto"))
