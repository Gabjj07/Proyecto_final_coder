from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime
from django.shortcuts import render

def mi_vista(request):
    return HttpResponse('Hola soy la vista')
def inicio(request):
    return HttpResponse('Soy la pantalla de inicio')
def vista_datos1(request):
    return HttpResponse('datos')
def primer_template(request):
    fecha_actual=datetime.now()
    datos={'fecha_actual': fecha_actual}
    return render(request, 'primer_template.html', datos)
