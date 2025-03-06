from django.urls import path
from .views import registro, iniciar_sesion, cerrar_sesion, perfil
from . import views

urlpatterns = [
    path('registro/', registro, name='registro'),
    path('login/', iniciar_sesion, name='login'),
    path('logout/', cerrar_sesion, name='logout'),
    path('perfil/', perfil, name='perfil'),
    path('signup/', views.signup, name='signup'),
]
