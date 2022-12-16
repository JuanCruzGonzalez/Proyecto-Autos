from django.shortcuts import render, redirect
from PaginaAutos.models import *
from PaginaAutos.forms import *
from Accounts.models import *

from django.views.generic import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.
def Inicio(request):
    return render(request, 'PaginaAutos/index.html')

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


class AutoCrear(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'can_add_imagen_auto'
    login_url="/Accounts/Inicio-sesion"
    model = Auto
    success_url = '/autos/modelos'
    fields = ['nombre', 'marca', 'motor', 'modelo', 'imagen']

class AutosLista(ListView):
    model = Auto
    template_name = 'PaginaAutos/autos_list.html'

class AutoDetalle(DetailView):
    model = Auto
    template_name = 'PaginaAutos/auto_detalle.html'

class AutosUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'can_change_imagen_auto'
    model= Auto
    success_url = '/autos/modelos'
    fields = ['nombre', 'marca', 'motor', 'modelo', 'imagen']

class AutosBorrar(PermissionRequiredMixin, DeleteView):
    permission_required = 'can_delete_imagen_auto'
    model= Auto
    success_url = '/autos//modelos'

@login_required(login_url='/Accounts/Inicio-sesion')
def mensaje(request):   
    if request.method=="POST":

        formulario= MensajeFormulario(request.POST, files=request.FILES)
        if formulario.is_valid():
            data=formulario.cleaned_data

            usuario=request.user

            mess=Mensaje(user=usuario, mensaje=data["mensaje"])
            mess.save()

            return render(request, 'PaginaAutos/mensaje_form.html',{"form":formulario, "errors":formulario.errors})
        
    formulario= MensajeFormulario()

    return render(request, 'PaginaAutos/mensaje_form.html',{"form":formulario} )
    
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


class MarcaDetalle(DetailView):
    model = Marca
    template_name = 'PaginaAutos/marca_detalle.html'
    