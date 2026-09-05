from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Empleado

# Create your views here.

def empleado(request):
    lista_empleados = Empleado.objects.all().order_by('nombre')

    # template = loader.get_template('empleados.html')

    # context = {
    #     'empleados': lista_empleados,
    # }

    # return HttpResponse(template.render(context, request))
    return render(request, 'empleados.html', {'empleados': lista_empleados})

def insertar_empleado(request):
    template = loader.get_template('insertar_empleado.html')
    return HttpResponse(template.render())