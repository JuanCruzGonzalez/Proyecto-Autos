from django.shortcuts import render, redirect
from Accounts.models import *
from Accounts.forms import *
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
                return render(request, "Accounts/login.html", {"form": formulario, "errors": "Credenciales invalidas"})
        else:
                return render(request, "Accounts/login.html", {"form": formulario, "errors": formulario.errors})


    formulario = AuthenticationForm()
    return render(request, "Accounts/login.html", {"form":formulario, "errors": errors}) 

def registrar_usuario(request):
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():
            
            formulario.save()
            return redirect("autos-inicio")
        else:
            return render(request, "Accounts/register.html", {"form": formulario, "errors": formulario.errors})

    formulario = UserRegisterForm()

    return render(request, "Accounts/register.html", {"form": formulario})

@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == "POST":
        formulario = UserEditForm(request.POST)
        if formulario.is_valid:
            
            información = formulario.cleaned_data

            usuario.email = información['email']
            usuario.password1 = información['password1']
            usuario.password2 = información['password2']
            usuario.save

            return render(request, "Accounts/index.html")

    else: 

        formulario = UserEditForm(initial={'email':usuario.email, })

    return render(request, "Accounts/editar_perfil.html", {"form":formulario, "usuario":usuario})

@login_required
def avatar(request):
    if request.method=="POST":

        formulario= AvatarForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            data=formulario.cleaned_data

            usuario=request.user

            avatar=Avatar(user=usuario, imagen=data["imagen"])
            avatar.save()

            return redirect("autos-inicio")
        
        else:
            return render(request, 'Accounts/agregar_avatar.html',{"form":formulario, "errors":formulario.errors})

    formulario= AvatarForm()

    return render(request, 'Accounts/agregar_avatar.html',{"form":formulario} )
