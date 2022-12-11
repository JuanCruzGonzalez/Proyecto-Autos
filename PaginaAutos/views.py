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
    return render(request, 'PaginaAutos/chat-global.html')

def Nosotros(request):
    return render(request, 'PaginaAutos/nosotros.html')

def Contacto(request):
    return render(request, 'PaginaAutos/contacto.html')

def resultado_buscar_autos(request):
    if request.GET:
        nombre=request.GET["nombre_alumno"]
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
    fields = ['nombre', 'marca', 'motor', 'modelo']

class AutosLista(ListView):
    model = Auto
    template_name = 'PaginaAutos/autos_list.html'

class AutoDetalle(DetailView):
    model = Auto
    template_name = 'PaginaAutos/auto_detalle.html'

class AutosUpdate(UpdateView):
    model= Auto
    success_url = '/autos/inicio'
    fields = ['nombre', 'marca', 'motor', 'modelo']

class AutosBorrar(DeleteView):
    model= Auto
    success_url = '/autos/inicio'

def CrearAutos(request):
    return render(request, "PaginaAutos/crear_autos.html")

def imagen_auto(request):
    if request.method=="POST":

        formulario= ImagenForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()

            return redirect("autos-inicio")
        
        else:
            return render(request, 'PaginaAutos/agregar_avatar.html',{"form":formulario, "errors":formulario.errors})

    return render(request,'PaginaAutos/agregar_imagen.html', locals())
