from django.urls import path
from stock import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('about/', views.about, name="About"),
    path('not_ready/', views.vendedor, name="Vendedores"),
    path('not_ready/', views.operador, name="Operadores"),
    path('item_listar/', views.ItemListView.as_view(), name="ListarItem"),
    path('item_detalle/<int:pk>/', views.ItemDetailView.as_view(), name="VerItem"),
    path('item_buscar/', views.busca_item, name="BuscarItem"),
    path('item_crear/', views.ItemCreateView.as_view(), name="CrearItem"),
    path('item_editar/<int:pk>/', views.ItemUpdateView.as_view(), name="ActualizarItem"),
    path('item_borrar/<int:pk>/', views.ItemDeleteView.as_view(), name="BorrarItem"),
]
