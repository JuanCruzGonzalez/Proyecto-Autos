from django import forms
#Registro de Usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AutosFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    marca = forms.CharField(max_length=100)
    modelo = forms.CharField(max_length=100)
    motor = forms.CharField(max_length=100)

class ImagenForm(forms.Form):
    imagen= forms.ImageField()