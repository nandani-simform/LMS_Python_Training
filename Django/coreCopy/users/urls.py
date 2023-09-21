from . import views
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('register/', views.CustomRegistrationView.as_view(), name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
]