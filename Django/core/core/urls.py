
from django.contrib import admin
from django.urls import path
from home.views import *

urlpatterns = [
    path('', home, name='home'), 
    path('contact/', contact, name='contact'), 
    path('about/', about, name='about'), 

    path('success-page/', success_page, name='success-page'), 
    
    path('admin/', admin.site.urls),
]
