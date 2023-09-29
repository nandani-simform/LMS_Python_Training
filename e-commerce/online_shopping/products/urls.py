
from django.urls import path, include
from .views import (AddProductView,
                    AddCategoryView,
                    DeleteProductView
                    
                    )


urlpatterns = [
    path('api/product/add', AddProductView.as_view()),
    
    path('api/product/delete/<int:product_id>/', DeleteProductView.as_view(), name='delete-product'),

    path('api/category/new', AddCategoryView.as_view()),


    
]