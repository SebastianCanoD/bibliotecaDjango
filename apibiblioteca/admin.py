from django.contrib import admin
from apibiblioteca.models import Autor, Categoria, Libro
# Register your models here.

# Registrar los modelos en el panel de administración
admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Libro)
