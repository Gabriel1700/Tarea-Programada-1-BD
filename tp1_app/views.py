from django.shortcuts import render, redirect 
from django.db import connection              
from django.contrib import messages            
from .models import Empleado    

# Create your views here.

def empleado(request):
    with connection.cursor() as cursor:
        cursor.execute("EXEC ObtenerEmpleados")
        columnas = [col[0].lower() for col in cursor.description]
        lista_empleados = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    return render(request, 'empleados.html', {'empleados': lista_empleados})

def insertar_empleado(request):
    if request.method == 'POST': #Si el método es post
        nombre = request.POST.get('nombre')  #Extrae la info de los inputs
        salario = request.POST.get('salario')

        with connection.cursor() as cursor: #conexión con la base de datos

            #envío de orden de ejecución del procedimiento almacenado, con los valores de nombre y salario extraídos anteriormente
            cursor.execute('EXEC dbo.InsertarEmpleado @Nombre=%s, @Salario=%s', [nombre, salario])

            #pide el resultado que da el procedimiento almacenado [codigo, msg] y lo guarda en variable fila 
            fila = cursor.fetchone()

            codigo = fila[0] if fila else -3
            mensaje = fila[1] if fila else "Error inesperado en el servidor."

        if codigo == 1: # = insercion exitosa
            messages.success(request, mensaje)
        else: # = insercion no exitosa
            messages.error(request, mensaje)

        return redirect('/insertar_empleado/')
        
    return render(request, 'insertar_empleado.html') 