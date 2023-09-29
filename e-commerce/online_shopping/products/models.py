from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=30, unique=True)
    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.ManyToManyField(Category, related_name='products')
    brand = models.CharField(max_length=50)
    rating = models.IntegerField()
    availability = models.BooleanField()
    
    def __str__(self):
        return self.product_name
    


