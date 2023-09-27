from django.contrib import admin
from django.urls import path
from tasks.views import TaskListCreateView, TaskRUDView


urlpatterns = [
    path("admin/", admin.site.urls),
    path('tasks/', TaskListCreateView.as_view()),
    path('tasks/<int:pk>/', TaskRUDView.as_view())



]
