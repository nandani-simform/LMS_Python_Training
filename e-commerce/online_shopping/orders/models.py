from django.db import models
from user.models import CustomUser
from shopping_cart.models import CartItem


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2) 
    shipping_address = models.CharField(max_length=200)
    cart_item = models.ForeignKey(CartItem, on_delete=models.CASCADE)

    def __str__(self):
        return self.order_date
    