from django.urls import path
from .views import register, profile
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register', register, name='user_register'),
    path('login', auth_views.LoginView.as_view(
        template_name='users/login.html'), name='user_login'),
    path('logout', auth_views.LogoutView.as_view(
        template_name='users/logout.html'), name='user_logout'),
    path('profile', profile, name='user_profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
