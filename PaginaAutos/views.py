from django.shortcuts import render, redirect
from PaginaAutos.models import *
from PaginaAutos.forms import *

from django.views.generic import *
from django.contrib.auth.forms import AuthenticationForm
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
    return render(request, 'PaginaAutos/motores.html')

def Nosotros(request):
    return render(request, 'PaginaAutos/nosotros.html')

def Contacto(request):
    return render(request, 'PaginaAutos/contacto.html')

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

#class AutosUpdate(LoginRequiredMixin, UpdateView):
class AutosUpdate(UpdateView):
    model= Auto
    success_url = '/autos/inicio'
    fields = ['nombre', 'marca', 'motor', 'modelo', 'imagen']

#class AutosBorrar(LoginRequiredMixin, DeleteView):
class AutosBorrar(DeleteView):
    model= Auto
    success_url = '/autos/inicio'

def CrearAutos(request):
    return render(request, "PaginaAutos/crear_autos.html")

class MarcaDetalle(DetailView):
    model = Marca
    template_name = 'PaginaAutos/marca_detalle.html'