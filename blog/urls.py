from django.urls import path
from . import views  # Importamos las vistas de la app 'blog'

urlpatterns = [
    path('', views.lista_posts, name='home'),  # Página principal del blog que muestra todos los posts
    path('crear_post/', views.crear_post, name='create_post'),  # Página para crear un nuevo post
]
