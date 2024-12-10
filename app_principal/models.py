from django.db import models

# Clase para representar autores
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

# Clase para representar libros
class Libro(models.Model):
    titulo = models.CharField(max_length=150)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    fecha_publicacion = models.DateField()

    def __str__(self):
        return self.titulo

# Clase para representar lectores
class Lector(models.Model):
    nombre = models.CharField(max_length=100)
    libros_prestados = models.ManyToManyField(Libro, blank=True)

    def __str__(self):
        return self.nombre

