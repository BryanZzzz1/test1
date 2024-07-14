from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from carro.carro import Carro
from .forms import AutoForm 
from .models import Auto 




# Create your views here.


def home(request):
    
    carro= Carro(request)

    return render(request,"ProyectoWebApp/home.html")


def lista_autos(request):
    autos = Auto.objects.all()
    return render(request, 'lista_autos.html', {'autos': autos})

def detalle_auto(request, auto_id):
    auto = get_object_or_404(Auto, pk=auto_id)
    return render(request, 'detalle_auto.html', {'auto': auto})

def crear_auto(request):
    if request.method == 'POST':
        form = AutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_autos')
    else:
        form = AutoForm()
    return render(request, 'crear_auto.html', {'form': form})


def actualizar_auto(request, pk):
    auto = get_object_or_404(Auto, pk=pk)
    if request.method == 'POST':
        form = AutoForm(request.POST, instance=auto)
        if form.is_valid():
            form.save()
            return redirect('lista_autos')
    else:
        form = AutoForm(instance=auto)
    
    return render(request, 'actualizar_auto.html', {'form': form})

def eliminar_auto(request, pk):
    auto = get_object_or_404(Auto, pk=pk)
    if request.method == 'POST':
        auto.delete()
        return redirect('lista_autos')
    # Puedes manejar una solicitud GET para confirmar la eliminación, si es necesario
    return render(request, 'eliminar_auto.html', {'auto': auto})


