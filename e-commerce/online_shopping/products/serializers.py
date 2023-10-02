from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    # categories = CategorySerializer(many=True, read_only=True)
    # category = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

        # fields = ('id','product_name','description','price','categories','brand','rating')

    # def get_category(self, obj):    
    #     return obj.brand
    





