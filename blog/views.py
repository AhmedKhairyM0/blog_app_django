from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Post

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


