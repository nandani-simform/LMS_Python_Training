from django.contrib import admin
from django.urls import path
from . import views
from .views import AllBlogsView, PostCreateView, PostDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.firstpage, name='first-page'),
    path('about/', views.about, name="about"),

    path('allblogs/', AllBlogsView.as_view(), name='all-blogs'),
    path('post/new/', PostCreateView.as_view(), name='blog-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='blog-detail'),

]
