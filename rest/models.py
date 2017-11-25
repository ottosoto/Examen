from django.db import models
from django.contrib import admin
from django.utils import timezone

class Plato(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Menu(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.CharField(max_length=100)
    platos = models.ManyToManyField(Plato, through='Descripcion')
    def __str__(self):
        return self.nombre

class Descripcion (models.Model):
    plato = models.ForeignKey(Platos, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

class DetalleInLine(admin.TabularInline):
    model = Detalle
    extra = 1
