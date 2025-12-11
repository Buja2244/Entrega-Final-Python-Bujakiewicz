from django.shortcuts import render, redirect
from .models import Marca, Proveedor, Celular
from .forms import MarcaForm, ProveedorForm, CelularForm

def inicio(request):
    return render(request, 'Web_App/inicio.html')

def crear_marca(request):
    if request.method == 'POST':
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = MarcaForm()
    
    return render(request, 'Web_App/formulario_creacion.html', {'form': form, 'modelo_nombre': 'Marca'})

def crear_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ProveedorForm()
    
    return render(request, 'Web_App/formulario_creacion.html', {'form': form, 'modelo_nombre': 'Proveedor'})

def crear_celular(request):
    if request.method == 'POST':
        form = CelularForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = CelularForm()
    
    return render(request, 'Web_App/formulario_creacion.html', {'form': form, 'modelo_nombre': 'Celular'})

def buscar_celular(request):
    return render(request, 'Web_App/buscar_celular.html')

def resultado_busqueda_celular(request):
    if request.GET.get('modelo_celular'):
        
        modelo_a_buscar = request.GET.get('modelo_celular')
        resultados = Celular.objects.filter(modelo__icontains=modelo_a_buscar)
        
        return render(request, 'Web_App/resultado_busqueda.html', {
            'celulares': resultados, 
            'termino': modelo_a_buscar
        })
    
    return render(request, 'Web_App/resultado_busqueda.html', {'celulares': []})