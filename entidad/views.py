from django.shortcuts import render, redirect
from django.http import HttpResponse
import sqlite3
from .forms import RopaForm
from .models import Ropa

# Create your views here.

def index(request, template_name='entidad/index.html'):
    dato = {"contacto": "http://127.0.0.1:8000/contacto"}
    return render(request, template_name, dato)

def shop(request, template_name='entidad/shop.html'):
    dato = {"saludo": "Bienvenido"}
    return render(request, template_name, dato)

def contacto(request, template_name="entidad/contacto.html"):
    return render(request, template_name)

def remeras(request, template_name='entidad/remeras.html'):
    remeras_list = Ropa.objects.all()
    dato = {"remeras": remeras_list}
    return render(request, template_name, dato)

#django reconoce id como primary key, accedo a un solo registro

def remera(request, id_ropa, template_name="entidad/remera.html"):
    remera_selec = Ropa.objects.get(id=id_ropa)
    dato = {"remera": remera_selec}
    return render(request, template_name, dato)

#carga de registros

def nueva_remera(request, template_name="entidad/remera_form.html"):
    if request.method == 'POST':
        form = RopaForm(request.POST)
        if form.is_valid():
            Ropa.objects.create(
                marca=form.cleaned_data["marca"],
                talle=form.cleaned_data["talle"],
                color=form.cleaned_data["color"],
                lisa=form.cleaned_data["lisa"],
                genero=form.cleaned_data["genero"])
            return redirect("remeras")
    else:
        form = RopaForm()
    dato = {"form": form}
    return render(request, template_name, dato)
    

