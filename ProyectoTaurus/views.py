from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from productosApp.models import Producto  # Importar el modelo Producto

def home(request):
    # Verificar los roles del usuario autenticado
    es_admin = request.user.is_authenticated and request.user.rol == 'admin'
    es_empleado = request.user.is_authenticated and request.user.rol == 'empleado'
    es_usuario = request.user.is_authenticated and request.user.rol == 'usuario'

    # Obtener todos los productos para mostrarlos en la página principal
    productos = Producto.objects.all()

    # Renderizar la plantilla con los datos necesarios
    return render(request, 'index.html', {
        'es_admin': es_admin,
        'es_empleado': es_empleado,
        'es_usuario': es_usuario,
        'productos': productos  # Pasar los productos al contexto
    })
