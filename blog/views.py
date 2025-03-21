from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Post
from django.shortcuts import render
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'blog/lista_posts.html'
    context_object_name = 'posts'
    ordering = ['-fecha_publicacion']

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detalle_post.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/crear_post.html'
    fields = ['titulo', 'contenido', 'imagen']
    success_url = reverse_lazy('home')  # Redirige al home después de crear el post

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/editar_post.html'
    fields = ['titulo', 'contenido', 'imagen']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.autor

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/eliminar_post.html'
    success_url = reverse_lazy('lista_posts')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.autor
def lista_posts(request):
    posts = Post.objects.all()  # Obtiene todos los posts
    return render(request, 'blog/lista_posts.html', {'posts': posts})