from django.shortcuts import render, redirect
from .models import Autor, Libro
from .forms import AutorForm, LibroForm, BuscarForm

# Vista para mostrar el inicio
def inicio(request):
    return render(request, 'app_principal/inicio.html')

# Vista para agregar autores
def agregar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = LibroForm()
    return render(request, 'app_principal/agregar.html', {'form': form, 'entidad': 'Libro'})

# Vista para buscar libros
def buscar_libro(request):
    form = BuscarForm()
    resultados = None
    if 'titulo' in request.GET:
        titulo = request.GET['titulo']
        resultados = Libro.objects.filter(titulo__icontains=titulo)
    return render(request, 'app_principal/buscar.html', {'form': form, 'resultados': resultados})

# Vista para listar todos los libros
def listar_libros(request):
    libros = Libro.objects.all()
    return render(request, 'app_principal/listar_libros.html', {'libros': libros})
