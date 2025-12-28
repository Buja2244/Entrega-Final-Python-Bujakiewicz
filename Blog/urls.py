from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('pages/', views.BlogList.as_view(), name='Pages'),
    path('pages/<int:pk>/', views.BlogDetail.as_view(), name='detalle_blog'),
    path('pages/crear/', views.crear_blog, name='crear_blog'),
    path('pages/editar/<int:id>/', views.editar_blog, name='editar_blog'),
    path('pages/eliminar/<int:id>/', views.eliminar_blog, name='eliminar_blog'),
    path('about/', views.acerca_de_mi, name='About'),
    path('buscar/', views.buscador, name='Buscador'),
]