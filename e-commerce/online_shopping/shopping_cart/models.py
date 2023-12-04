from django.db import models
from products.models import Product
from user.models import CustomUser

class Cart(models.Model):
    usercart = models.OneToOneField(CustomUser,null=True, on_delete=models.CASCADE,verbose_name="user name")
    products = models.ManyToManyField(Product, through='CartItem')

    def __str__(self):
        return f"Cart {self.pk} for {self.usercart.username}"
    
    class Meta:
        db_table = "cart"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, null =True, on_delete=models.CASCADE, verbose_name="user cart")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} * {self.product.product_name} in {self.cart.usercart.username}'s cart"

    class Meta:
        db_table = "cartitem"
