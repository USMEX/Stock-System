from django.shortcuts import render
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from Apps.worker.models import worker, job
from .forms import *
from django.contrib.auth.decorators import login_required
from .decorators import user_auth, allowed_users
from django.shortcuts import redirect
from django.contrib import messages

# |-----| |-----| |-----| DASHBOARD DE INICIO   |-----| |-----| |-----|
# |-----| View que permite visualizar la página de inicio al    |-----| 
# |-----| estar logueado correctamente.                         |-----|
# |-----------------------------------------------------------|
@login_required(login_url='workerLogin')
def homeDashboard(request):
    context = {'home': 'active'}
    return render(request, 'dashboard.html', context)

# |-----------------------------------------------------------|
# |-| Este apartado cuenta con la lista de trabajadores     |-|
# |-| registrados en el sistema, solo podrá visualizarse    |-|
# |-| con permisos de administrador.                        |-|
# |-----------------------------------------------------------|
@login_required(login_url='workerLogin')
@allowed_users(allowed_roles=['admin'])
def workerList(request):
    Workers = worker.objects.all()
    context = {'workerList': 'active', 'workers':Workers}
    return render(request, 'worker/list.html', context)

# |-----| |-----| |-----| PERFIL DEL USUARIO    |-----| |-----| |-----|
# |-----| Permitirá la visualización de los perfiles de los     |-----| 
# |-----| usuarios.                                             |-----|
# |-----------------------------------------------------------|
@login_required(login_url='workerLogin')
def workerProfile(request):
    Job = job.objects.filter(jobWorker = request.user.worker.pk)
    HasJob = False
    if job.objects.filter(jobWorker = request.user.worker.pk).count()>0:
        HasJob = True
    context = {'workerProfile': 'active', 'job': Job, 'hasJob': HasJob}
    return render(request, 'worker/profile.html', context)

# |-----| |-----| |-----| LOGIN DE USUARIO      |-----| |-----| |-----|
# |-----| Página que permitirá el inicio de sesión del usuario. |-----|
# |-----------------------------------------------------------|
@user_auth
def workerLogin(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            text = 'Welcome back ' + request.user.worker.workerNameFirst
            messages.success(request, text)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
            
    context = {}
    return render(request, 'worker/login.html', context)

# |-----| |-----| |-----| FORMULARIO DE REGISTRO|-----| |-----| |-----|
# |-----| Mediante este se permitirá el registro de nuevos      |-----| 
# |-----| usuarios, tomando en cuenta que estarán asociados     |-----|
# |-----| a una cuenta de django.contrib.                       |-----|
# |-----------------------------------------------------------|
@user_auth
def workerRegister(request):
    
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        
        text = 'Please, sign in'
        messages.success(request, text)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            
            group = Group.objects.get(name='worker')
            user.groups.add(group)
            
            worker.objects.create(
                user = user,
                workerEmail =     user.username,
                workerNickname =  user.username,
                workerNameFirst = user.first_name,
                workerNameLast =  user.last_name,
            )
            
    context = {'workerRegister': 'active', 'form': form}
    return render(request, 'worker/register.html', context)

# |-----| |-----| |-----| CIERRE DE SESIÓN      |-----| |-----| |-----|
# |-----------------------------------------------------------|
def workerLogout(request):
    logout(request)
    return redirect('workerLogin')