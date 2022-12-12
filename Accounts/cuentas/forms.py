from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Usuario', widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name= forms.CharField(label='Apellido', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Correo electronico', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirme la contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name','last_name', 'email', 'username','password1', 'password2']

