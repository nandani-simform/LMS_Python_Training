from django.shortcuts import render
from rest_framework.views import APIView
from shopping_cart.serializers import CartItemSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from rest_framework import status
from shopping_cart.models import Cart, CartItem
from products.models import Product

from user.models import CustomUser
from django.shortcuts import get_object_or_404


class AddToCartView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        user = request.user
        print(user) # user 1

        product_id = request.data.get('product')
        print(product_id)
    
        try:
            product = Product.objects.get(pk = product_id)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        cart, created = Cart.objects.get_or_create(usercart = user)

        cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)

        if not item_created:
            cart_item.quantity += 1
            cart_item.save()

        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class ViewCartView(APIView): 
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        print(user)

        cart_items = Cart.objects.filter(user=user)
        serializer = CartItemSerializer(cart_items, many=True)
        product_list = serializer.data
        data = [{'cart_id': item['id'], 'product_id': item['product'], 'quantity': item['quantity']} for item in product_list]


        return Response(data, status=status.HTTP_200_OK)
    
    
class UpdateCartView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, cart_id):
        user = request.user
        try:
            cart_item = Cart.objects.get(id=cart_id)
        except Cart.DoesNotExist:
            return Response({"error": "Cart item not found"}, status=status.HTTP_404_NOT_FOUND)
        
        new_quantity = request.data.get('quantity')
        if new_quantity is not None:
            cart_item.quantity = new_quantity
            cart_item.save()

            serializer = CartSerializer(cart_item)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response({"error": "Invalid request data"}, status=status.HTTP_400_BAD_REQUEST)

class RemoveItemCartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, cart_id):
        item = Cart.objects.get(id=cart_id)
        serializer = CartSerializer(item)
        return Response(serializer.data)


    def delete(self, request, cart_id):
        try:
            item = Cart.objects.get(id=cart_id)
            item.delete()
            return Response({'message': 'Item removed successfully.'}, status=status.HTTP_204_NO_CONTENT)
        except Cart.DoesNotExist:
            raise Http404('Cart item does not exist')

class EmptyCartView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        user = request.user
        Cart.objects.filter(user=user).delete()

        return Response({"message: Cart is now empty."}, status=status.HTTP_204_NO_CONTENT)