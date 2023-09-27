
from django.contrib import admin
from django.urls import path
from demo.views import index


urlpatterns = [
    path("index", index, name='index'),
    path("admin/", admin.site.urls),
]
