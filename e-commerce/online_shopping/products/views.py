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
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
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
    # def get(self,request, product_id):
    #     id = product_id
    #     # breakpoint()
    #     if id is not None: 
    #         product = Product.objects.get(id=product_id)
    #         serializer = ProductSerializer(product)
    #         return Response(serializer.data)

    
    def delete(self, request, product_id):
        try:
            # breakpoint()
            product = Product.objects.get(id=product_id)
            product.delete()
            return Response({'message': 'Product deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
            raise Http404("Product does not exist")