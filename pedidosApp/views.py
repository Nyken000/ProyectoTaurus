from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Carrito, ItemCarrito
from productosApp.models import Producto

@login_required
def ver_carrito(request):
    carrito, creado = Carrito.objects.get_or_create(usuario=request.user)
    total_carrito = sum(item.total_item() for item in carrito.items.all())
    return render(request, 'pedidos/ver_carrito.html', {
        'carrito': carrito,
        'total_carrito': total_carrito,
    })


@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito, creado = Carrito.objects.get_or_create(usuario=request.user)
    item, item_creado = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
    if not item_creado:
        item.cantidad += 1
        item.save()
    messages.success(request, f"'{producto.nombre}' ha sido añadido al carrito.")
    return redirect('ver_carrito')

@login_required
def eliminar_item_carrito(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id, carrito__usuario=request.user)
    item.delete()
    messages.success(request, "El producto ha sido eliminado del carrito.")
    return redirect('ver_carrito')

@login_required
def actualizar_cantidad(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id, carrito__usuario=request.user)
    nueva_cantidad = request.POST.get('cantidad')
    if nueva_cantidad.isdigit() and int(nueva_cantidad) > 0:
        item.cantidad = int(nueva_cantidad)
        item.save()
        messages.success(request, "La cantidad del producto ha sido actualizada.")
    else:
        messages.error(request, "Cantidad inválida.")
    return redirect('ver_carrito')
