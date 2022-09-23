from django.shortcuts import render
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from django.contrib.auth.models import Group
from apps.worker.models import worker
from .forms import *
from django.contrib.auth.decorators import login_required
from .decorators import user_auth, allowed_users


# Página principal del portal
@login_required(login_url='workerLogin')
def homeDashboard(request):
    context = {'home': 'active'}
    return render(request, 'dashboard.html', context)

# Listado de usuarios registrados
@login_required(login_url='workerLogin')
@allowed_users(allowed_roles=['admin'])
def workerList(request):
    context = {'workerList': 'active'}
    return render(request, 'worker/list.html', context)

# Listado de usuarios registrados
@login_required(login_url='workerLogin')
def workerProfile(request):
    context = {'workerProfile': 'active'}
    return render(request, 'worker/profile.html', context)

# Listado de usuarios registrados
@user_auth
def workerLogin(request):
    context = {'workerLogin': 'active'}
    return render(request, 'worker/login.html', context)

# Listado de usuarios registrados
@user_auth
def workerRegister(request):
    
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            email = username
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            
            group = Group.objects.get(name='worker')
            user.groups.add(group)
            worker.objects.create(
                user = user,
                workerEmail =     user.username,
                workerNameFirst = user.first_name,
                workerNameLast =  user.last_name,
            )
    context = {'workerRegister': 'active', 'form': form}
    return render(request, 'worker/register.html', context)