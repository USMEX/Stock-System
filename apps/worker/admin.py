from django.contrib import admin

# Register your models here.
from .models import worker

# |-----| Visualización de los campos de la tabla de trabajadores |-----| 
@admin.register(worker)
class workerList(admin.ModelAdmin):
    list_display = ["workerNameLast", "workerNameFirst", "workerEmail"]