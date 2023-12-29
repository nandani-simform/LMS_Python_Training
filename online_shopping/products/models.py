from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=30, unique=True)
    
    def __str__(self):
        return self.category_name

    class Meta:
        db_table = 'category'

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.ManyToManyField(Category, related_name='products') 
    
    def __str__(self):
        return f"product {self.pk}: {self.product_name}"
    
    class Meta:
        db_table = 'product'
