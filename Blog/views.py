from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Blog
from .forms import BlogForm
from django.views.generic import ListView, DetailView

# Pagina de inicio
def inicio(request):
    return render(request, 'Blog/inicio.html')

class BlogList(LoginRequiredMixin, ListView):
    model = Blog
    template_name = "Blog/pages.html"
    context_object_name = "blogs"

# Detalles
class BlogDetail(LoginRequiredMixin, DetailView):
    model = Blog
    template_name = "Blog/detalle_blog.html"
    context_object_name = "blog"

# About
def acerca_de_mi(request):
    return render(request, "Blog/about.html")

# Crear Blog
@login_required
def crear_blog(request):
    if request.method == 'POST':
        formulario = BlogForm(request.POST, request.FILES)
        if formulario.is_valid():
            blog = formulario.save(commit=False)
            blog.autor = request.user
            blog.save()
            messages.success(request, "¡Entrada creada!")
            return redirect('Pages')
    else:
        formulario = BlogForm()
    return render(request, 'Blog/crear_blog.html', {'formulario': formulario})

# Eliminar blog
@login_required
def eliminar_blog(request, id):
    blog = get_object_or_404(Blog, id=id)
    
    if blog.autor == request.user or request.user.is_superuser:
        blog.delete()
        messages.success(request, "Entrada eliminada.")
    else:
        messages.error(request, "No tienes permiso para eliminar esta entrada.")
        
    return redirect('Pages')

# Editar blog
@login_required
def editar_blog(request, id):
    blog = get_object_or_404(Blog, id=id)
    
    if blog.autor != request.user and not request.user.is_superuser:
        messages.error(request, "No tienes permiso para editar esta entrada.")
        return redirect('Pages')

    if request.method == 'POST':
        formulario = BlogForm(request.POST, request.FILES, instance=blog)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "¡Entrada actualizada!")
            return redirect('Pages')
    else:
        formulario = BlogForm(instance=blog)
        
    return render(request, "Blog/editar_blog.html", {"formulario": formulario, "blog": blog})



def buscador(request):
    criterio = request.GET.get('criterio', '')
    resultados = Blog.objects.filter(titulo__icontains=criterio) if criterio else []
    return render(request, "Blog/resultados_busqueda.html", {"resultados": resultados, "criterio": criterio})