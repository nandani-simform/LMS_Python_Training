
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('', include('products.urls')),
    path('', include('shopping_cart.urls')),
    # path('', include('orders.urls')),

]
