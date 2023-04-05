from django.urls import path
from .views import PostListView, PostDetailView, CreatePostView

urlpatterns = [
    path('post/new', CreatePostView.as_view(), name='post_new'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('', PostListView.as_view(), name='home'),
]
