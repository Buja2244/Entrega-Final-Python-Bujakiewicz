from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_request, name='Login'),
    path('salir/', views.cerrar_sesion, name='Logout'),
    path('registro/', views.registro_usuario, name='Registro'),
    path('editar/', views.editar_perfil, name='EditarPerfil'),
    path('cambiar-contrasenia/', views.CambiarContrasenia.as_view(), name='CambiarContrasenia'),
    path('agregar-avatar/', views.agregar_avatar, name='agregar_avatar'),
]