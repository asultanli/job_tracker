from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from applications import views as app_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('applications.urls')),
    path('accounts/register/', app_views.register, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]