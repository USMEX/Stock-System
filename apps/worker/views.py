from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Página principal del portal
def homeDashboard(request):
    return render(request, 'dashboard.html')

# Listado de usuarios registrados
def workerList(request):
    return render(request, '/worker/List.html')