from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistroForm, PerfilForm, UserUpdateForm 
from .models import Perfil
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            Perfil.objects.create(usuario=usuario)  # 🔹 Crea el perfil automáticamente
            login(request, usuario)  # 🔹 Inicia sesión automáticamente después del registro
            return redirect('lista_posts')
    else:
        form = RegistroForm()
    
    return render(request, 'accounts/registro.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'  # Usa tu template de login
    redirect_authenticated_user = True  # Si el usuario ya está logueado, lo redirige
    def get_success_url(self):
        return reverse_lazy('perfil') 

def cerrar_sesion(request):
    logout(request)
    return redirect('home')

@login_required
def perfil(request):
    perfil, created = Perfil.objects.get_or_create(usuario=request.user)  # 🔹 Asegura que el perfil existe
    return render(request, 'accounts/perfil.html', {'perfil': perfil})

@login_required
def editar_perfil(request):
    perfil, created = Perfil.objects.get_or_create(usuario=request.user)  # 🔹 Asegura que el perfil existe

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        perfil_form = PerfilForm(request.POST, request.FILES, instance=perfil)

        if user_form.is_valid() and perfil_form.is_valid():
            user_form.save()
            perfil_form.save()
            return redirect('perfil')

    else:
        user_form = UserUpdateForm(instance=request.user)
        perfil_form = PerfilForm(instance=perfil)

    return render(request, 'accounts/editar_perfil.html', {
        'user_form': user_form,
        'perfil_form': perfil_form
    })