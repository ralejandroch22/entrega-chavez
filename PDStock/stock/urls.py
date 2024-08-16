from django.urls import path
from stock import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('listar/', views.ItemListView.as_view(), name="ListarItem"),
    path('item_buscar/', views.busca_item, name="BuscarItem"),
    path('item_crear/', views.ItemCreateView.as_view(), name="CrearItem"),
    path('item_editar/<pk>/', views.ItemUpdateView.as_view(), name="ActualizarItem"),
    path('item_borrar/<pk>/', views.ItemDeleteView.as_view(), name="BorrarItem"),
]
