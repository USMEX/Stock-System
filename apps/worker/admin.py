from django.contrib import admin

# Register your models here.
from .models import worker, department, jobTittle, job

# |-----| Visualización de los campos de la tabla de trabajadores |-----| 
@admin.register(worker)
class workerList(admin.ModelAdmin):
    list_display = ["workerNameLast", "workerNameFirst", "workerEmail"]
    
# |-----| Visualización de los campos de la tabla de departamentos |-----| 
@admin.register(department)
class departmentList(admin.ModelAdmin):
    list_display = ["dptoNameLong"]
    
# |-----| Visualización de los campos de la tabla de departamentos |-----| 
@admin.register(jobTittle)
class jobTittleList(admin.ModelAdmin):
    list_display = ["jobtName"]
    
# |-----| Visualización de los campos de la tabla de departamentos |-----| 
@admin.register(job)
class jobsList(admin.ModelAdmin):
    list_display = ["jobWorker", "jobJobTittle"]