
from django.urls import path, include
from .views import (
                        AddToCartView,
                        ViewCartView,
                        
                    )

urlpatterns = [
    path("api/cart/add/<int:product_id>", AddToCartView.as_view()),
    path("api/cart/view", ViewCartView.as_view()),
    path("api/cart/update/<int:cart_id>", ViewCartView.as_view()),

]