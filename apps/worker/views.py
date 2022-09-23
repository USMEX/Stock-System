from django.shortcuts import render
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from apps.worker.models import worker
from .forms import *


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
    
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('workerEmail')
            
            group = Grou.object.get(name='worker')
            user.groups.add(group)
            worker.objects.create(
                workerEmail =     user.email,
                workerNameFirst = user.first_name,
                workerNameLast =  user.last_name,
                workerDateReg =   user.date_joined,
            )
    context = {'workerRegister': 'active', 'form': form}
    return render(request, 'worker/register.html', context)