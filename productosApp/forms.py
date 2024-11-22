from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock', 'imagen']
        widgets = {
            'imagen': forms.TextInput(attrs={'placeholder': 'Ruta relativa (ej. img/nombre-imagen.jpg)'}),
        }
