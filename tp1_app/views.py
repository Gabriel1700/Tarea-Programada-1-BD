from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def empleado(request):
    return HttpResponse("Lista de empleados")

def insertar_empleado(request):
    return HttpResponse("Insertar empleados")
