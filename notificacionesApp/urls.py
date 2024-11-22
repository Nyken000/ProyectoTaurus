from django.urls import path
from . import views  # Importa las vistas de la aplicación

urlpatterns = [
    # Ejemplo de ruta para una vista llamada "lista_notificaciones"
    path('', views.lista_notificaciones, name='lista_notificaciones'),
]
