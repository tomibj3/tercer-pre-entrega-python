# Tercer-pre-entrega-python

Pasos Realizados:

1) Se creó un entorno virtual (python -m venv env)
2) Se creó un proyecto llamado "mi_proyecto"
3) Se creó la app "app_principal"
4) La app app_principal se registró en el archivo settings.py en la lista INSTALLED_APPS.
5) Se definieron tres modelos en app_principal/models.py (Agregar Libro, Buscar Libro y Listar Libros)
6) Se realizaron las migraciones necesarias (python manage.py makemigrations) & (python manage.py migrate)
7) Se crearon formularios en app_principal/forms.py para manejar datos
8) En app_principal/views.py, se implementaron las vistas para agregar, buscar y listar libros
9) En app_principal/urls.py, se configuraron las rutas para las vistas correspondientes
10) Se crearon plantillas HTML en app_principal/templates/app_principal/
