from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='posts/', blank=True, null=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('detalle_post', kwargs={'pk': self.pk})  # Redirige al post creado