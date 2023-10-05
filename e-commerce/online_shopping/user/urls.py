
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
                        UserRegisterView, 
                        UserView, 
                        UserLoginView, 
                        UserLogoutView,
                        UserDetailsView
                    
                    )
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('api/user/<int:pk>', UserView.as_view(), name='user-detail'),
    path('api/user', UserView.as_view(), name='user-list' ),

    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

    path('api/auth/user', UserDetailsView.as_view(), name='user-detail' ),
    path('api/auth/register', UserRegisterView.as_view(), name='user-register'),
    path('api/auth/login', UserLoginView.as_view(), name='user-login'),
    path('api/auth/logout', UserLogoutView.as_view(), name='user-logout')

   
]