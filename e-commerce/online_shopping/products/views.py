from django.shortcuts import render
from .serializers import CategorySerializer, ProductSerializer
from rest_framework.views import APIView
from .models import Product, Category
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404

class AddCategoryView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
    

class AddProductView(APIView):
    # def get(self, request):
    #     products = Product.objects.all()
    #     serializer = ProductSerializer(products, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            item = serializer.save()
            return Response(
                {
                    "product_id": item.id,
                    "product_name": item.product_name,
                    "message": "New product created",
                }, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DeleteProductView(APIView):
    def delete(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)
            product.delete()
            return Response({'message': 'Product deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
            raise Http404("Product does not exist")
        
class ProductDetailView(APIView):
    def get(self, request, product_id=None):
        id = product_id
        if id is not None: 
            item = Product.objects.get(id=product_id)
            serializer = ProductSerializer(item)
            return Response(serializer.data)
        
        item = Product.objects.order_by('id')
        serializer = ProductSerializer(item, many=True)
        return Response(serializer.data)
    
    def put(self, request, product_id):
        # id = product_id
        item = Product.objects.get(id=product_id)
        serializer = ProductSerializer(item, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Product data updated'}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, product_id):
        # id = product_id
        try:
            item = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(item, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Product partial data updated'}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryBasedProductView(APIView):
    def get(self, request, category_id):
        try:
            category = Category.objects.get(id=category_id)
            product = Product.objects.filter(categories = category)
            serialiser = ProductSerializer(product, many=True)
            item = serialiser.data
            list = [product['product_name'] for product in item]
            return Response(list)
            
        except Category.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)



    