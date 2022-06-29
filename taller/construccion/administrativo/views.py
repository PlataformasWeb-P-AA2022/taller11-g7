from contextlib import redirect_stderr
from django.shortcuts import render,redirect
from django.template import RequestContext
from django.shortcuts import render

# Create your views here.

from administrativo.models import *
from administrativo.forms import *

def index(request):
    edificios = Edificio.objects.all()
    informacion_template = {'edificio':edificios, 'numero_edificios': len(edificios)}
    return render(request, 'index.html',informacion_template)

def obtener_edificio(request, id):
    edificios = Edificio.objects.get(pk=id)
    informacion_template = {'edificio':edificios}
    return render(request, 'obtener_edificio.html', informacion_template)

def crear_edificio(request):
    if request.method =='POST':
        formulario = EdificioForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
        else :
            formulario = EdificioForm()
        diccionario = {'formulario':formulario}

        return render(request, 'crear_edificio.html',diccionario)

def editar_edificio(request, id):
    edificio = Edificio.objects.get(pk=id)
    if request.method=='POST':
        formulario = EdificioForm(request.POST, instance=edificio)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
        else:
            formulario = EdificioForm(instance=edificio)
        diccionario = {'formulario': formulario}

    return render(request, 'editar_edificio.html', diccionario)

def eliminar_edificio(request, id):
    edificio = Edificio.objects.get(pk=id)
    edificio.delete()
    return redirect(index)

def crear_departamento(request):
    if request.method=='POST':
        formulario = DepartamentoForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = DepartamentoForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crear_departamento.html', diccionario)

def editar_departamento(request, id):
    edificio = Edificio.objects.get(pk=id)
    if request.method=='POST':
        formulario = DepartamentoForm(request.POST, instance=edificio)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = DepartamentoForm(instance=edificio)
    diccionario = {'formulario': formulario}

    return render(request, 'editar_departamento.html', diccionario)

def eliminar_departamento(request,id):
    edificio = Edificio.objects.get(pk=id)
    edificio.delete()
    return redirect(index)

def crear_departamento_edificio(request,id):
    edificio = Edificio.objects.get(pk=id)
    if request.method=='POST':
        formulario = DepartamentoEdificioForm(edificio, request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = DepartamentoEdificioForm(edificio)
    diccionario = {'formulario': formulario, 'edificio': edificio}

    return render(request, 'crear_departamentoEdificio.html', diccionario)


