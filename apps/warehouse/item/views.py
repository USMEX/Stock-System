from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# View de listado de intems
def itemLobby(request):
    return HttpResponse('Lobby de items')

# View de listado de intems
def itemList(request):
    return HttpResponse('Listado de items')

# Visualización de items individuales
def itemDesc(request, elementId):
    return HttpResponse('Visualización de item ' + elementId)