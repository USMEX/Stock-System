from django.contrib import admin

# Register your models here.
from .models import worker

@admin.register(worker)
class univList(admin.ModelAdmin):
    list_display = ["workerNameLast", "workerNameFirst", "workerEmail"]