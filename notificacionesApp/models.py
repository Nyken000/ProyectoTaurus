from django.db import models

class Notificacion(models.Model):
    usuario_id = models.IntegerField()  # Guardamos solo el ID del usuario como referencia
    mensaje = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    leida = models.BooleanField(default=False)

    @property
    def usuario(self):
        from usuariosApp.models import Usuario  # Importación diferida
        return Usuario.objects.get(id=self.usuario_id)  # Recupera el usuario cuando se accede a él

    def __str__(self):
        return f"Notificación para {self.usuario.username} - {'Leída' if self.leida else 'No leída'}"
