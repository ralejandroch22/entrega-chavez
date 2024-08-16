from django.contrib import admin
from stock.models import Item, Vendedor, Operador
# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    list_display = ("nombre","marca",)
    list_filter = ("nombre","marca",)
    ordering = ("nombre","marca",)

class OperadorAdmin(admin.ModelAdmin):
    list_display = ("nombre","apellido","email",)
    list_filter = ("nombre","apellido","email",)
    ordering = ("nombre","apellido","email",)

class VendedorAdmin(admin.ModelAdmin):
    list_display = ("nombre","apellido","email",)
    list_filter = ("nombre","apellido","email",)
    ordering = ("nombre","apellido","email",)


admin.site.register(Item, ItemAdmin)
admin.site.register(Operador, OperadorAdmin)
admin.site.register(Vendedor, VendedorAdmin)