from django.urls import path
from apps.worker import views

urlpatterns = [
 path('', views.homeDashboard, name='home'),
 path('users/', views.workerList, name='workerList'),
 path('users/profile', views.workerProfile, name='workerProfile'),
 path('users/register', views.workerRegister, name='workerRegister'),
 path('users/login', views.workerLogin, name='workerLogin'),
 path('users/logout', views.workerLogout, name='workerLogout'),
 ]