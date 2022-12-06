from django.urls import path   
from PaginaAutos.views import *
from PaginaAutos import views

urlpatterns = [
    path('inicio/', Inicio, name='autos-inicio'),
 ]
