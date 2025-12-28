from django.shortcuts import render, redirect
from django.contrib.auth import login, logout as django_logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import EditarUsuarioForm
from .forms import RegistroUsuarioForm
from .forms import AvatarForm
from .models import Avatar

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("inicio")
        else:
            messages.error(request, "Usuario o contraseña incorrectos")
    
    form = AuthenticationForm()
    form.fields['username'].label = "Nombre de Usuario"
    form.fields['password'].label = "Contraseña"
    
    return render(request, "Cuentas/login.html", {"form": form})

def cerrar_sesion(request):
    django_logout(request)
    return redirect("inicio")

def registro_usuario(request):
    if request.method == 'POST':
        formulario = RegistroUsuarioForm(request.POST, request.FILES) 
        if formulario.is_valid():
            user = formulario.save()
            imagen = formulario.cleaned_data.get('imagen')
            if imagen:
                Avatar.objects.create(user=user, imagen=imagen)
                
            messages.success(request, "¡Usuario Creado!")
            return redirect("Login")
    else:
        formulario = RegistroUsuarioForm() 
    return render(request, "Cuentas/registro.html", {"form": formulario})

@login_required
def editar_perfil(request):
    usuario = request.user
    if request.method == 'POST':
        formulario = EditarUsuarioForm(request.POST, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "¡Perfil actualizado!")
            return redirect('inicio')
    else:
        formulario = EditarUsuarioForm(instance=usuario)
    
    return render(request, "Cuentas/editar_usuario.html", {"form": formulario})

class CambiarContrasenia(PasswordChangeView):
    template_name = 'Cuentas/cambiar_contrasenia.html'
    success_url = reverse_lazy('inicio')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['old_password'].label = "Contraseña actual"
        form.fields['new_password1'].label = "Nueva contraseña"
        form.fields['new_password2'].label = "Confirmar nueva contraseña"

        form.fields['new_password1'].help_text = """
        <ul>
            <li>Tu contraseña no puede ser muy similar a tu información personal.</li>
            <li>Debe contener al menos 8 caracteres.</li>
            <li>No puede ser una contraseña muy común.</li>
            <li>No puede ser totalmente numérica.</li>
        </ul>
    """
        return form
    
@login_required
def agregar_avatar(request):
    if request.method == "POST":
        formulario = AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
            Avatar.objects.filter(user=request.user).delete()
            
            avatar = Avatar(user=request.user, imagen=formulario.cleaned_data["imagen"])
            avatar.save()
            return redirect("inicio")
    else:
        formulario = AvatarForm()
    return render(request, "cuentas/agregar_avatar.html", {"formulario": formulario})