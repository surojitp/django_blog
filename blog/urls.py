from django.urls import path
from .views import home, about

urlpatterns = [
    path('', home, name='blog_home'),
    path('about', about, name='about_about'),
]
