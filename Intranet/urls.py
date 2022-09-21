from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    # Redireccionamiento a app de items
    path('', lambda req: redirect('/items/')),
    path('admin/', admin.site.urls),
    path('items/', include('apps.warehouse.item.urls')),
]