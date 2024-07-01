from django.db import models
from django.contrib.auth import get_user_model
from tienda.models import Producto
from django.db.models import F, Sum, FloatField

User = get_user_model()  

class Pedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) 
    @property
    def total(self):
        total_pedido = self.lineas_pedido.aggregate(
            total=Sum(F("producto_id__precio") * F("cantidad"), output_field=FloatField())
        )["total"]
        return total_pedido or 0

    class Meta:
        db_table = "pedidos"
        verbose_name = "pedido"
        verbose_name_plural = "pedidos"
        ordering = ['id']


class LineaPedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido_id = models.ForeignKey(Pedido, related_name='lineas_pedido', on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cantidad} unidades de {self.producto_id.nombre}"

    class Meta:
        db_table = "lineas_pedidos"
        verbose_name = "linea de pedido"
        verbose_name_plural = "lineas de pedido"
        ordering = ['id']
