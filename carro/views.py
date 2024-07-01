from django.shortcuts import render,redirect

from .carro import Carro
from tienda.models import Producto
from .models import ConfiguracionCarro


# Create your views here.

def agregar_producto(request,producto_id):
    carro= Carro(request)
    producto= Producto.objects.get(id=producto_id)

    carro.agregar(producto=producto)
    
    return redirect("Tienda")



def eliminar_producto(request,producto_id):
    carro= Carro(request)
    producto= Producto.objects.get(id=producto_id)

    carro.eliminar_carrito(producto=producto)
    
    return redirect("Tienda")





def restar_producto(request,producto_id):
    carro= Carro(request)
    producto= Producto.objects.get(id=producto_id)

    carro.restar_producto(producto=producto)
    
    return redirect("Tienda")


def limpiar_carroproducto(request):
    carro= Carro(request)
    carro.limpiar_carrito()
    
    return redirect("Tienda")



def activar_desactivar_carro(request):
    configuracion = ConfiguracionCarro.objects.first()
    if request.method == 'POST':
        configuracion.activo = not configuracion.activo
        configuracion.save()
        return redirect('pagina_principal')  
    return render(request, 'carro/activar_desactivar_carro.html', {'configuracion': configuracion})


def mostrar_carro(request):
    configuracion = ConfiguracionCarro.objects.first()
    if configuracion.activo:
        carro = Carro(request)
       
        contexto = {
            'carro': carro
        }
        return render(request, 'carro/mostrar_carro.html', contexto)
    else:
       
        return render(request, 'carro/carro_desactivado.html')