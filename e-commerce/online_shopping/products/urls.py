
from django.urls import path, include
from .views import (AddProductView,
                    AddCategoryView,
                    DeleteProductView,
                    ProductDetailView,
                    CategoryBasedProductView
                    
                    )

urlpatterns = [
    path('api/product/new', AddProductView.as_view()),
    
    path('api/product/<int:product_id>', ProductDetailView.as_view()),
    path('api/product/all', ProductDetailView.as_view()),

    path('api/product/update/<int:product_id>', ProductDetailView.as_view()),
    path('api/product/delete/<int:product_id>', DeleteProductView.as_view()),

    path('api/category/new', AddCategoryView.as_view()),
    path('api/category/<int:category_id>', CategoryBasedProductView.as_view()),

    
]