from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views  

urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta para el administrador de Django
    path('', views.home, name='home'),  # Página principal
    path('usuarios/', include('usuariosApp.urls')),  # URLs de usuariosApp
    path('productos/', include('productosApp.urls')),  # Registro de URLs de productos
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
