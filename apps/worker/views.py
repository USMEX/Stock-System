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

# Listado de usuarios registrados
def workerProfile(request):
    context = {'workerProfile': 'active'}
    return render(request, 'worker/profile.html', context)

# Listado de usuarios registrados
def workerLogin(request):
    context = {'workerLogin': 'active'}
    return render(request, 'worker/login.html', context)

# Listado de usuarios registrados
def workerRegister(request):
    context = {'workerRegister': 'active'}
    return render(request, 'worker/register.html', context)