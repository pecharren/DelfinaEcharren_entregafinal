from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

def lista_posts(request):
    posts = Post.objects.all()  
    return render(request, 'blog/lista_posts.html', {'posts': posts})

# Vista para crear un nuevo post
def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirige a la página principal después de guardar el post
    else:
        form = PostForm()
    return render(request, 'blog/crear_post.html', {'form': form})
