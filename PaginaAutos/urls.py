from django.urls import path   
from PaginaAutos.views import *
from PaginaAutos import views

urlpatterns = [
    path('inicio/', Inicio, name='autos-inicio'),
    path('modelos/', Autos, name='autos-modelos'),
    path('marcas/', Marcas, name='autos-marcas'),
    path('motores/', Motores, name='autos-motores'),
    path('contacto/', Contacto, name='contacto'),
    path('autos/crear/', AutoCrear.as_view(), name="autos-crear"),
    path('cursos/detalle/<pk>', AutoDetalle.as_view(), name="autos-detalle"),
    path('autos/list/', AutosLista.as_view(), name="autos-list"),
    path('cursos/actualizar/<pk>', AutosUpdate.as_view(), name="autos-update"),
    path('cursos/borrar/<pk>', AutosBorrar.as_view(), name="autos-borrar"),
    path('sobre-nosotros/', Nosotros, name='sobre-nosotros'),
 ]
