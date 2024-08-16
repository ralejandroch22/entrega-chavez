from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from stock.models import Item
from stock.forms import BuscaItemForm
# Create your views here.

def inicio(request):
    return render(request, "stock/index.html")

@login_required
def busca_item(request):

    if request.method == "POST":
        miFormulario = BuscaItemForm(request.POST) 

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            
            items = Item.objects.filter(nombre__icontains=informacion["item"])

            return render(request, "stock/item_mostrar.html", {"items": items})
    else:
        miFormulario = BuscaItemForm()

    return render(request, "stock/item_buscar.html", {"miFormulario": miFormulario})

class ItemListView(LoginRequiredMixin, ListView):
    model = Item
    context_object_name = "items"
    template_name = "stock/listar.html"

class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    template_name = "stock/item_crear.html"
    success_url = reverse_lazy('ListarItem')
    fields = ['nombre', 'marca', 'precio','imagen']

class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    template_name = "stock/item_editar.html"
    success_url = reverse_lazy('ListarItem')
    fields = ['nombre', 'marca', 'precio']

class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = Item
    template_name = "stock/item_borrar.html"
    success_url = reverse_lazy('ListarItem')