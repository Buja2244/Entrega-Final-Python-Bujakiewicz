from django import forms
from .models import Marca, Proveedor, Celular

# Marca
class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nombre', 'pais_origen']
        
# Proveedor
class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'telefono', 'email']

# Celular
class CelularForm(forms.ModelForm):
    class Meta:
        model = Celular
        fields = ['modelo', 'precio', 'stock', 'marca', 'proveedor']