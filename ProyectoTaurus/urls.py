from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views  # Asegúrate de tener la vista `home` en views.py

urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta para el administrador de Django
    path('', views.home, name='home'),  # Página principal
    path('usuarios/', include('usuariosApp.urls')),  # URLs de usuariosApp
    path('productos/', include('productosApp.urls')),  # Registro de URLs de productos
    path('notificaciones/', include('notificacionesApp.urls')),  # Opcional: Si ya tienes notificacionesApp
    path('pedidos/', include('pedidosApp.urls')),  # Opcional: Si ya tienes pedidosApp
    path('notificaciones/', include('notificacionesApp.urls')), 
    path('pedidos/', include('pedidosApp.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
