from django.urls import path
from Accounts.cuentas.views import *  
from django.contrib.auth.views import LogoutView

urlspatters = [
path('Inicio-sesion/', Login, name="auth-login" ),
path('register/', registrar_usuario, name="auth-register" ),
path("logout/",LogoutView.as_view(template_name="templates/logout.html"), name="auth-logout"),
]