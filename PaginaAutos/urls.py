from django.urls import path   
from PaginaAutos.views import *
from PaginaAutos import views

urlpatterns = [
    path('inicio/', Inicio, name='autos-inicio'),
    path('modelos/', Autos, name='autos-modelos'),
    path('marcas/', Marcas, name='autos-marcas'),
    path('motores/', Motores, name='autos-motores'),
    path('contacto/', Contacto, name='contacto'),
    path('sobre-nosotros/', Nosotros, name='sobre-nosotros'),
 ]
