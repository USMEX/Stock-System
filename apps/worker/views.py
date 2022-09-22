from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Página principal del portal
def homeDashboard(request):
    context = {'home': 'active'}
    return render(request, 'dashboard.html', context)

# Listado de usuarios registrados
def workerList(request):
    context = {'workerList': 'active'}
    return render(request, 'worker/list.html', context)