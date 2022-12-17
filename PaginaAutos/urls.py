from django.urls import path   
from PaginaAutos.views import *
from django.contrib.auth.views import LogoutView
from Accounts.urls import *
urlpatterns = [
    path('inicio/', Inicio, name='autos-inicio'),
    path('modelos/', Autos, name='autos-modelos'),
    path('marcas/', MarcaLista.as_view(), name='marcas-list'),
    path('chat/', mensaje, name='autos-chat'),
    path('chat/list', MensajeLista.as_view(), name='chat-list'),
    path('contacto/', Contacto, name='contacto'),
    path('autos/crear/', AutoCrear.as_view(), name="autos-crear"),
    path('autos/detalle/<pk>', AutoDetalle.as_view(), name="autos-detalle"),
    path('marcas/detalle/<pk>', MarcaDetalle.as_view(), name="marcas-detalle"),
    path('autos/list/', AutosLista.as_view(), name="autos-list"),
    path('autos/actualizar/<pk>', AutosUpdate.as_view(), name="autos-update"),
    path('autos/borrar/<pk>', AutosBorrar.as_view(), name="autos-borrar"),
    path('sobre-nosotros/', Nosotros, name='sobre-nosotros'),
    path('buscar/autos/', resultado_buscar_autos, name='resultado-buscar-auto'),
    # path('editar/imagen-auto/', imagen_auto, name='editar-imagen-auto'),
 ]
