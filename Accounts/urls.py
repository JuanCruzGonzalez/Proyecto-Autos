from django.urls import path
from Accounts.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
path('Inicio-sesion/', Login, name='auth-login' ),
path('register/', registrar_usuario, name='auth-register' ),
path('logout/',LogoutView.as_view(template_name='Accounts/logout.html'), name='auth-logout'),
path('editarPerfil/', editarPerfil, name='auth-edit'),
path('editar/avatar/', avatar, name='editar-avatar')
]