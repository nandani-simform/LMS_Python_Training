from django.contrib import admin
from django.urls import path
from . import views
from .views import AllBlogsView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView


urlpatterns = [
    path('', views.firstpage, name='first-page'),
    path('about/', views.about, name="about"),

    path('allblogs/', AllBlogsView.as_view(), name='all-blogs'),
    path('post/new/', PostCreateView.as_view(), name='blog-create'),
    path('post/<int:blog_id>/',PostDetailView.as_view(), name='blog-detail'),
    path('post/<int:blog_id>/update',PostUpdateView.as_view(), name='blog-update'),
    path('post/<int:blog_id>/delete',PostDeleteView.as_view(), name='blog-delete'),

    path('accessdenied/', views.accessDenied, name='access-denied'),
    
]
