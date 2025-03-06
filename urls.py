```python
from django.urls import path
from .views import lista_posts, crear_post

urlpatterns = [
    path('', lista_posts, name='lista_posts'),
    path('nuevo/', crear_post, name='crear_post'),
]
```