from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post
from django.urls import reverse_lazy

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class CreatePostView(CreateView):
    model = Post
    fields = ['title', 'body', 'author']
    template_name = 'blog/post_new.html'

class UpdatePostView(UpdateView):
    model = Post
    fields = ['title', 'body']
    template_name = 'blog/post_edit.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('home')