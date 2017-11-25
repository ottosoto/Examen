# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

from django.contrib import messages
from .forms import PlatilloForm
from peliculas.models import Platos, Ventas, Menus

def platillo_editar(request):
    if request.method == "POST":
        formulario = PlatilloForm(request.POST)
        if formulario.is_valid():
            menus = Platos.objects.create(nombre=formulario.cleaned_data['nombre'], descripcion = formulario.cleaned_data['descripcion'])
            for plato_id in request.POST.getlist('platos'):
                menus = menus(plato_id=platos_id, ventas_id = ventas.id)
                actuacion.save()
            messages.add_message(request, messages.SUCCESS, 'Pelicula Guardada Exitosamente')
    else:
        formulario = PeliculaForm()
    return render(request, 'peliculas/pelicula_editar.html', {'formulario': formulario})
