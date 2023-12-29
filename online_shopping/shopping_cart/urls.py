
from django.urls import path, include
from .views import (
                        AddToCartView,
                        ViewCartView,
                        UpdateCartView,
                        RemoveItemCartView,
                        EmptyCartView
                        
                    )

urlpatterns = [
    path("api/cart/add", AddToCartView.as_view()),
    path("api/cart/view", ViewCartView.as_view()),
    path("api/cart/update/<int:cart_id>", UpdateCartView.as_view()),
    path("api/cart/remove/<int:cart_id>", RemoveItemCartView.as_view()),
    path("api/cart/empty", EmptyCartView.as_view()),

]