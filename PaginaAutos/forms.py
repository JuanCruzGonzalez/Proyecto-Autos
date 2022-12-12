from django import forms
from .models import *
#Registro de Usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AutosFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    marca = forms.CharField(max_length=100)
    modelo = forms.CharField(max_length=100)
    motor = forms.CharField(max_length=100)
    imagen = forms.ImageField()

    class Meta:
        model= Auto
        fields=['nombre', 'marca', 'modelo', 'motor', 'imagen']

class MensajeFormulario(forms.Form):
    class Meta:
        model= Mensaje
        fields=['mensaje']

