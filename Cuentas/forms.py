from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import Avatar

class EditarUsuarioForm(UserChangeForm):
    password = None
    username = forms.CharField(label="Nombre de Usuario", widget=forms.TextInput(attrs={'class': 'form-control'}), help_text="")
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label="Nombre", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label="Apellido", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {
            'username': 'Nombre de Usuario',
            'email': 'Correo Electrónico',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
        }

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(label="Correo Electrónico", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    imagen = forms.ImageField(required=False)
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["username", "email"]
        labels = {
            'username': 'Nombre de Usuario',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = "Contraseña"
        self.fields['password2'].label = "Confirmar contraseña"
        
        for field in self.fields:
            self.fields[field].help_text = ""
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']