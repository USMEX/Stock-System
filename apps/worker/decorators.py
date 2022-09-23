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