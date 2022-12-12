from django.shortcuts import render, redirect
from PaginaAutos.models import *
from PaginaAutos.forms import *

from django.views.generic import *
from django.contrib.auth.forms import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.
def Inicio(request):
    return render(request, 'PaginaAutos/index.html')

def Autos(request):
    return render(request, 'PaginaAutos/autos.html')

def Marcas(request):
    return render(request, 'PaginaAutos/marcas.html')

def Chat(request):
    return render(request, 'PaginaAutos/chat-global.html')

def Nosotros(request):
    return render(request, 'PaginaAutos/nosotros.html')

def Contacto(request):
    return render(request, 'PaginaAutos/contacto.html')

def resultado_buscar_autos(request):
    if request.GET:
        nombre=request.GET["nombre"]
        if(nombre != ''):
            autos=Auto.objects.filter(nombre__icontains=nombre)
            return render(request, 'PaginaAutos/resultado_buscar_auto.html',{"autos":autos})
        else:
            return render(request, 'PaginaAutos/resultado_buscar_auto.html',{"autos":[]})
    else:
            return render(request, 'PaginaAutos/resultado_buscar_auto.html',{"autos":[]})

class AutoCrear(CreateView):
    model = Auto
    success_url = '/autos/inicio'
    fields = ['nombre', 'marca', 'motor', 'modelo', 'imagen']

class AutosLista(ListView):
    model = Auto
    template_name = 'PaginaAutos/autos_list.html'

class AutoDetalle(DetailView):
    model = Auto
    template_name = 'PaginaAutos/auto_detalle.html'

class AutosUpdate(UpdateView):
    model= Auto
    success_url = '/autos/inicio'
    fields = ['nombre', 'marca', 'motor', 'modelo', 'imagen']

class AutosBorrar(DeleteView):
    model= Auto
    success_url = '/autos/inicio'

def CrearAutos(request):
    return render(request, "PaginaAutos/crear_autos.html")

class MensajeCrear(CreateView):
    model = Mensaje
    success_url = '/autos/chat'
    fields = ['mensaje']
    
class MensajeLista(ListView):
    model = Mensaje
    template_name = 'PaginaAutos/agregar_imagen.html'


    