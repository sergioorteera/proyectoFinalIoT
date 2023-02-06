from django.http import HttpResponse
from django.shortcuts import render


def bienvenida(request):
    return render(request, "producto.html",{})
