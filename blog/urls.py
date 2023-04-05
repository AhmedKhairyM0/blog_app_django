from django.urls import path
from .views import PostListView, PostDetailView, CreatePostView, UpdatePostView

urlpatterns = [
    path('post/new', CreatePostView.as_view(), name='post_new'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit', UpdatePostView.as_view(), name='post_edit'),
    path('', PostListView.as_view(), name='home'),
]
