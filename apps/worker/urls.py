from django.urls import path
from apps.worker import views

urlpatterns = [
    # Redireccionamiento a app de items
 path('', views.homeDashboard, name='home'),
 path('users/', views.workerList, name='itemList'),
 ]