from django.db import models
from user.models import CustomUser
from shopping_cart.models import CartItem
from django.db.models import Sum
from decimal import Decimal



class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2) 
    shipping_address = models.CharField(max_length=200)
    cart_item = models.ForeignKey(CartItem, on_delete=models.CASCADE)


    def calculate_total_amount(self):
        cart_items_total = self.cart_item.aggregate(total=Sum(models.F('product__price') * models.F('quantity'), output_field=models.DecimalField()))
        self.total_amount = cart_items_total['total'] or Decimal('0.00')

    def __str__(self):
        return self.order_date
    