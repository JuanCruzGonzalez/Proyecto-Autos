from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AvatarForm(forms.Form):
    imagen= forms.ImageField(required=False)

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

class UserEditForm(forms.Form):
    username = forms.CharField(label='Modificar username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Modificar nombre', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name= forms.CharField(label='Modificar apellido', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Modificar E-mail',  widget=forms.EmailInput(attrs={'class': 'form-control'}))
    #password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    #password2 = forms.CharField(label='Repetir la contraseña',  widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        
        model = User
        fields = ['first_name','last_name', 'email', 'username','password1', 'password2']

        help_text = {'email': 'Indica un correo electronico que uses habitualmente', 'password1': 'La contraseña no puede ser la misma que la anterior'}

