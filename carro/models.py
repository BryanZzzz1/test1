

from django.db import models
from tienda.models import Producto  

class ConfiguracionCarro(models.Model):
    activo = models.BooleanField(default=False)

    def __str__(self):
        return "Configuración del Carro"
