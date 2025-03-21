from django.urls import path
from .views import registro, CustomLoginView , cerrar_sesion, perfil, editar_perfil
from . import views

urlpatterns = [
    path('registro/', registro, name='registro'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', cerrar_sesion, name='logout'),
    path('perfil/', perfil, name='perfil'),
     path('signup/', registro, name='signup'),
    path('editar_perfil/', editar_perfil, name='editar_perfil'),
]
