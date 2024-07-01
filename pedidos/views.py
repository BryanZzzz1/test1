from django.shortcuts import render
from django.http import HttpResponse

def pedidos(request):

    return HttpResponse("Esta es la página de pedidos. Aquí puedes mostrar información relevante.")
