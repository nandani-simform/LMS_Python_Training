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
from django.shortcuts import get_object_or_404


class AddToCartView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the data to the Cart model
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ViewCartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        cart_items = CartItem.objects.filter(user=user)
        serializer = CartItemSerializer(cart_items, many=True)
        product_list = serializer.data
        data = [{'cart_id': item['id'], 'product_id': item['product'], 'quantity': item['quantity']} for item in product_list]


        return Response(data, status=status.HTTP_200_OK)
    
    
class UpdateCartView(APIView):
    permission_classes = [IsAuthenticated]

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
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response({"error": "Invalid request data"}, status=status.HTTP_400_BAD_REQUEST)

class RemoveItemCartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, cart_id):
        item = CartItem.objects.get(id=cart_id)
        serializer = CartItemSerializer(item)
        return Response(serializer.data)


    def delete(self, request, cart_id):
        try:
            item = CartItem.objects.get(id=cart_id)
            item.delete()
            return Response({'message': 'Item removed successfully.'}, status=status.HTTP_204_NO_CONTENT)
        except CartItem.DoesNotExist:
            raise Http404('Cart item does not exist')

class EmptyCartView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        user = request.user
        CartItem.objects.filter(user=user).delete()

        return Response({"message: Cart is now empty."}, status=status.HTTP_204_NO_CONTENT)