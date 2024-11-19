from django import forms
from usuariosApp.models import Usuario

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'telefono']
        widgets = {
            'password': forms.PasswordInput(),  # Ocultar contraseña al escribir
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # Encriptar la contraseña
        user.rol = 'admin'  # Asignar el rol "usuario" por defecto
        if commit:
            user.save()
        return user
