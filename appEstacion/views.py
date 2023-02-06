from django.shortcuts import render
from django.http import HttpResponse
from appEstacion.models import datoThingSpeak

def index(request):
    return render(request, 'quienes_somos.html')

def quienes_Somos(request):
    return render(request, 'quienes_somos.html')

def proyecto(request):
    return render(request, 'proyecto.html')

def producto(request):
    dato = datoThingSpeak.enviar(request)
    return render(request, 'producto.html',{'dato':dato})


def contacto(request):
    return render(request, 'contacto.html')

