from django.shortcuts import render, redirect
from Accounts.cuentas.models import *
from Accounts.cuentas.forms import *

from django.views.generic import *
from django.contrib.auth.forms import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.
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
                return render(request, "sessions/login.html", {"form": formulario, "errors": "Credenciales invalidas"})
        else:
                return render(request, "sessions/login.html", {"form": formulario, "errors": formulario.errors})


    formulario = AuthenticationForm()
    return render(request, "sessions/login.html", {"form":formulario, "errors": errors}) 

def registrar_usuario(request):
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():
            
            formulario.save()
            return redirect("autos-inicio")
        else:
            return render(request, "sessions/register.html", {"form": formulario, "errors": formulario})

    formulario = UserRegisterForm()

    return render(request, "sessions/register.html", {"form": formulario})

