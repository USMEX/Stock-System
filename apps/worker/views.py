from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Página principal del portal
def homeDashboard(request):
    return HttpResponse('Página principal')

# Listado de usuarios registrados
def workerList(request):
    return HttpResponse('Listado de trabajadores')