from django.urls import path
from apps.worker import views

urlpatterns = [
    # Redireccionamiento a app de items
 path('', views.homeDashboard, name='home'),
 path('users/', views.workerList, name='workerList'),
 path('users/profile', views.workerProfile, name='workerProfile'),
 path('users/login', views.workerLogin, name='workerLogin'),
 path('users/register', views.workerRegister, name='workerRegister'),
 ]