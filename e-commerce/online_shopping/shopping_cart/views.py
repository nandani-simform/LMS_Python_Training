from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import CartItemSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from rest_framework import status
from .models import CartItem
from products.models import Product
from user.models import CustomUser

class AddToCartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, product_id):
        user = request.user
        print(user)
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        cart_item, created = CartItem.objects.get_or_create(user=user, product=product)
        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class ViewCartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        cart_items = CartItem.objects.filter(user=user)
        serializer = CartItemSerializer(cart_items, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, cart_id):
        user = request.user
        try:
            cart_item = CartItem.objects.get(id=cart_id)
        except CartItem.DoesNotExist:
            return Response({"error": "Cart item not found"}, status=status.HTTP_404_NOT_FOUND)
        
        new_quantity = request.data.get('quantity')
        if new_quantity is not None:
            cart_item.quantity = new_quantity
            cart_item.save()

            serializer = CartItemSerializer(cart_item)
            return Response(serializer.data)

        return Response({"error": "Invalid request data"}, status=status.HTTP_400_BAD_REQUEST)


