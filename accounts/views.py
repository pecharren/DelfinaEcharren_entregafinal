from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm, PerfilForm
from .models import Perfil
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.set_password(form.cleaned_data['password'])
            usuario.save()
            Perfil.objects.create(usuario=usuario)  # Crea perfil automáticamente
            login(request, usuario)
            return redirect('home')
    else:
        form = RegistroForm()
    return render(request, 'accounts/registro.html', {'form': form})

def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        usuario = authenticate(request, username=username, password=password)
        if usuario:
            login(request, usuario)
            return redirect('home')
    return render(request, 'accounts/login.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('home')


@login_required
def perfil(request):
    perfil = request.user.perfil
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = PerfilForm(instance=perfil)
    return render(request, 'accounts/perfil.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo usuario
            messages.success(request, 'Tu cuenta ha sido creada exitosamente!')
            return redirect('login')  # Redirige a la vista de login
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario')
    else:
        form = UserCreationForm()
    
    return render(request, 'accounts/registro.html', {'form': form})

