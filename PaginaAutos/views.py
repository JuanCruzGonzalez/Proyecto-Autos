from django.shortcuts import render, redirect
from PaginaAutos.models import *
from PaginaAutos.forms import *
from Accounts.models import *

from django.views.generic import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
def Inicio(request):

    if request.user.is_authenticated:
        imagen_model = Avatar.objects.filter(user = request.user.id)[0]
        imagen_url = imagen_model.imagen.url
    else :
        imagen_url = ""

    return render(request, 'PaginaAutos/index.html', {"imagen_url": imagen_url})

def Autos(request):
    return render(request, 'PaginaAutos/autos.html')

def Marcas(request):
    return render(request, 'PaginaAutos/marcas.html')


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


class AutoCrear(LoginRequiredMixin,CreateView):
    login_url="/autos/Inicio-sesion/"
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

class MensajeCrear(LoginRequiredMixin,CreateView):
    login_url="/autos/Inicio-sesion/"
    model = Mensaje
    success_url = '/autos/chat'
    fields = ['mensaje']
    
class MensajeLista(ListView):
    model = Mensaje
    template_name = '/chat/list'

def Login(request):

    errors = []

    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            user = authenticate(username=data["username"], password =data["password"])

            if user is not None:
                login(request, user)
                return redirect("autos-inicio")
            
            else:
                return render(request, "PaginaAutos/login.html", {"form": formulario, "errors": "Credenciales invalidas"})
        else:
                return render(request, "PaginaAutos/login.html", {"form": formulario, "errors": formulario.errors})


    formulario = AuthenticationForm()
    return render(request, "PaginaAutos/login.html", {"form":formulario, "errors": errors}) 

def registrar_usuario(request):
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():
            
            formulario.save()
            return redirect("autos-inicio")
        else:
            return render(request, "PaginaAutos/register.html", {"form": formulario, "errors": formulario.errors})

    formulario = UserRegisterForm()

    return render(request, "PaginaAutos/register.html", {"form": formulario})

class MarcaDetalle(DetailView):
    model = Marca
    template_name = 'PaginaAutos/marca_detalle.html'
    