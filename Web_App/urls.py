from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    
    path('marca/crear/', views.crear_marca, name='marca_form'),
    path('proveedor/crear/', views.crear_proveedor, name='proveedor_form'),
    path('celular/crear/', views.crear_celular, name='celular_form'),
    path('celular/buscar/', views.buscar_celular, name='buscar_celular'),
    path('celular/resultados/', views.resultado_busqueda_celular, name='resultado_busqueda_celular'),
]