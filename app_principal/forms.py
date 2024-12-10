from django import forms
from .models import Autor, Libro, Lector

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'nacionalidad']

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'fecha_publicacion']

class LectorForm(forms.ModelForm):
    class Meta:
        model = Lector
        fields = ['nombre', 'libros_prestados']

class BuscarForm(forms.Form):
    titulo = forms.CharField(label='Título', max_length=150)
