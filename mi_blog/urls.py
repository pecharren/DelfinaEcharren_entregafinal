from django.contrib import admin
from django.urls import path, include  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # Asegúrate de incluir las URLs de la app accounts
    # otras rutas de la app 'blog', por ejemplo:
    path('', include('blog.urls')),
]