from django.urls import path
from apps.warehouse.item import views

urlpatterns = [
    # Redireccionamiento a app de items
 path('', views.itemLobby, name='itemHome'),
 path('list/', views.itemList, name='itemList'),
 path('item/<str:elementId>', views.itemDesc, name='itemDescription'),
 ]