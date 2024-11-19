from django.db import models
from django.contrib.auth import get_user_model  # Importación de get_user_model para evitar el problema de importación circular
from productosApp.models import Producto

# Obtener el modelo de usuario configurado
Usuario = get_user_model()

class Pedido(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=[('pendiente', 'Pendiente'), ('enviado', 'Enviado'), ('entregado', 'Entregado')])

    def __str__(self):
        return f"Pedido {self.id} - {self.usuario.username}"
    
class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.producto.nombre} - {self.cantidad} unidades"
