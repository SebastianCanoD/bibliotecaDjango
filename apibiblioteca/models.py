# Create your models here.
from django.db import models
# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    correo = models.EmailField(null=True, blank=True, verbose_name="Correo Electrónico")

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre de la Categoría")

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    descripcion = models.TextField(null=True, blank=True, verbose_name="Descripción")
    imagen = models.ImageField(upload_to='libros/', null=True, blank=True, verbose_name="Imagen")
    num_paginas = models.IntegerField(null=True, blank=True, verbose_name="Número de Páginas")
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, verbose_name="Autor")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoría")

    def __str__(self):
        return self.titulo
