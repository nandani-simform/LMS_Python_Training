
from django.urls import path, include
from .views import (UserRegisterView, 
                    UserListView, 
                    UserDetailView, 
                    UserView, 
                    UserLoginView, 
                    UserLogoutView,
                    UserDetailsView
                    
                    
                    )
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('api/user/<int:pk>/', UserView.as_view(), name='user-detail'),
    path('api/user', UserView.as_view(), name='user-list' ),

    path('api/auth/user', UserDetailsView.as_view(), name='user-detail' ),
    path('api/auth/register', UserRegisterView.as_view(), name='user-register'),
    path('api/auth/login', UserLoginView.as_view(), name='user-login'),
    path('api/auth/logout', UserLogoutView.as_view(), name='user-logout')

    # path('api/auth/register', UserListView.as_view()),
    # path('api/users/<int:pk>/', UserDetailView.as_view()),


]