from django.shortcuts import render,redirect

from .carro import Carrito
from tienda.models import Producto

# Create your views here.

def agregar_producto(request,producto_id):
    carro= Carrito(request)
    producto= Producto.objects.get(id=producto_id)

    carro.agregar(producto=producto)
    
    return redirect("tienda")



def eliminar_producto(request,producto_id):
    carro= Carrito(request)
    producto= Producto.objects.get(id=producto_id)

    carro.eliminar_carrito(producto=producto)
    
    return redirect("tienda")



def restar_producto(request,producto_id):
    carro= Carrito(request)
    producto= Producto.objects.get(id=producto_id)

    carro.restar_producto(producto=producto)
    
    return redirect("tienda")


def limpiar_carroproducto(request,producto_id):
    carro= Carrito(request)
    carro.limpiar_carrito()
    
    return redirect("tienda")



