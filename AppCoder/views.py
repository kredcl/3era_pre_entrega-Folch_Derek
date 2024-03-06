from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def inicio(request):

    return render(request, "inicio.html")

def about(request):

    return render(request, "about.html")

def login(request):

    return render(request, "login.html")

def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exito')  # se podria redirigir a cualquier pagimna, aqui mandamos el mensaje y ademas ponemos si desea agregar mas usuarios
    else:
        form = UsuarioForm()
    return render(request, 'crear_usuario.html', {'form': form})

def exito(request):
    return render(request, 'exito.html')

def exito_dueno(request):
    return render(request, 'exito_dueno.html')

def exito_resto(request):
    return render(request, 'exito_resto.html')

def crear_dueño(request):
    if request.method == 'POST':
        form = DueñoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exito_dueno')  # se podria redirigir a cualquier pagimna, aqui mandamos el mensaje y ademas ponemos si desea agregar mas usuarios
    else:
        form = DueñoForm()
    return render(request, 'crear_dueño.html', {'form': form})

def crear_resto(request):
    if request.method == 'POST':
        form = restoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exito_resto')  # se podria redirigir a cualquier pagimna, aqui mandamos el mensaje y ademas ponemos si desea agregar mas usuarios
    else:
        form = restoForm()
    return render(request, 'crear_resto.html', {'form': form})

def buscar_resto(request):

    return render(request, 'buscar_resto.html')

def resul_resto(request):

    restorantes = request.GET["nombre_rest"]

    resultados = resto.objects.filter(nombre__icontains=restorantes)

    return render(request, "resultados.html", {"resultados":resultados})