
# from django.contrib import admin
# from django.urls import path, include
# from home.views import *

# urlpatterns = [
#     # path('', home, name='home'), 
#     # path('contact/', contact, name='contact'), 
#     # path('about/', about, name='about'), 
#     # path('success-page/', success_page, name='success-page'), 
    
#     path('admin/', admin.site.urls),
#     path('', include('blog.urls')),
# ]

from django.contrib import admin
from django.contrib.auth import views as auth_view 
from django.urls import path, include
from users import views as user_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_view.register, name='register'),
    path('profile/', user_view.profile, name='profile'),
    path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('blog.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)