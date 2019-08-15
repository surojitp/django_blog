from django.urls import path
from .views import (
    home, 
    about, 
    PostListView, 
    PostDetailsView, 
    PostCreateView, 
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)

urlpatterns = [
    #path('', home, name='blog_home'),
    path('', PostListView.as_view(), name='blog_home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user_posts'),
    path('post/<int:pk>/', PostDetailsView.as_view(), name='post_details'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('about', about, name='about_about'),
]
