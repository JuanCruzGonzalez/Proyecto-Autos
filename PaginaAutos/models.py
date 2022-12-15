from django.db import models

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
    mensaje=models.CharField(max_length=150)
    def __str__(self) -> str:
        return f'{self.mensaje}'

class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    historia = models.CharField(max_length=100)
    fecha_creacion = models.DateField()
    pais = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.nombre} Creada el: {self.fecha_creacion.year} en {self.pais}. {self.historia} "