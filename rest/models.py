from django.db import models
from django.contrib import admin
from django.utils import timezone

class Platos(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Ventas(models.Model):
    nombrecliente = models.CharField(max_length=100)
    vendedor= models.ForeignKey('auth.user')
    platos = models.ForeignKey(Platos)
    def __str__(self):
        return self.nombrecliente

class Menus (models.Model):
    plato = models.ForeignKey(Platos, on_delete=models.CASCADE)
    venta = models.ForeignKey(Ventas, on_delete=models.CASCADE)
