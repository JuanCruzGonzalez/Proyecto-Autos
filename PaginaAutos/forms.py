from django import forms
from .models import *
#Registro de Usuario


class AutosFormulario(forms.Form):
    class Meta:
        model= Auto
        fields=['nombre', 'marca', 'modelo', 'motor', 'imagen']
