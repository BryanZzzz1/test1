from django.contrib import admin
from .models import CategoriadeProductos , Producto


class CategoriadeProductosAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")
    

class ProductodeProductosAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")


admin.site.register(CategoriadeProductos, CategoriadeProductosAdmin)

admin.site.register(Producto, ProductodeProductosAdmin)





