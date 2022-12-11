from django.urls import path   
from PaginaAutos.views import *
from PaginaAutos import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('inicio/', Inicio, name='autos-inicio'),
    path('modelos/', Autos, name='autos-modelos'),
    path('marcas/', Marcas, name='autos-marcas'),
    path('chat/', Chat, name='autos-chat'),
    path('contacto/', Contacto, name='contacto'),
    path('autos/crear/', AutoCrear.as_view(), name="autos-crear"),
    path('autos/detalle/<pk>', AutoDetalle.as_view(), name="autos-detalle"),
    path('autos/list/', AutosLista.as_view(), name="autos-list"),
    path('autos/actualizar/<pk>', AutosUpdate.as_view(), name="autos-update"),
    path('autos/borrar/<pk>', AutosBorrar.as_view(), name="autos-borrar"),
    path('sobre-nosotros/', Nosotros, name='sobre-nosotros'),
    path('buscar/autos/', resultado_buscar_autos, name='resultado-buscar-auto'),
    path('editar/imagen-auto/', imagen_auto, name='editar-imagen-auto'),
    path('Inicio-sesion/', Login, name="auth-login" ),
    path('register/', registrar_usuario, name="auth-register" ),
    path("logout/",LogoutView.as_view(template_name="PaginaAutos/logout.html"), name="auth-logout")
 ]
