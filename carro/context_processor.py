#from .carro import Carro

from requests import request


def importe_total_carro(request):
    total=0
 #   miCarro=Carro(request)
    #if request.user.is_authenticated:
        
    for key, value in request.session["carro"].items():        #key

        total=total+float(value['precio'])
            
    return {'importe_total_carro':total}   
        
