from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('agregar-libro/', views.agregar_libro, name='agregar_libro'),
    path('buscar-libro/', views.buscar_libro, name='buscar_libro'),
    path('listar-libros/', views.listar_libros, name='listar_libros'),
]

