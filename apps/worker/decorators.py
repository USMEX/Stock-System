from django.http import HttpResponse
from django.shortcuts import redirect

# |-----| |-----| |-----| USUARIO AUTENTIFICADO |-----| |-----| |-----|
# |-----| Decorador para validad que el usuaro se encuentre con |-----| 
# |-----| una sesión iniciada                                   |-----|
# |-----| |-----| |-----| |----| |----| |----|  |-----| |-----| |-----|
def user_auth(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, *kwargs)
    return wrapper_func

# |-----| |-----| |-----| PERMISOS DE USUARIO   |-----| |-----| |-----|
# |-----| Decorador que permite la entrada a el virew solo si   |-----| 
# |-----| cuenta con los permisos necesarios/                   |-----|
# |-----| |-----| |-----| |----| |----| |----|  |-----| |-----| |-----|
def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('home')
        return wrapper_func
    return decorator