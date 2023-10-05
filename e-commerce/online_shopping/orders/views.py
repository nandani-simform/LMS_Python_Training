from django.shortcuts import render
from django.db import transaction

from rest_framework.views import APIView

from .models import Order
from user.models import CustomUser
from products.models import Product
from shopping_cart.models import CartItem

from .serializers import OrderSerializers
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from decimal import Decimal 


class CheckoutView(APIView):
    def post(self,request):
        user = request.user
        cart = CartItem.objects.filter(user=user)
        total_amount = Decimal('0.00')
        for items in cart:
            product = items.product #items.product_id
            quantity = items.quantity
            pid = Product.objects.get(id=product)
            price = pid.price
            subtotal = quantity*price
            total_amount += subtotal 

        order_data = {
            'user': user,
            'total_amount': total_amount,
        }

        with transaction.atomic():
            order_serializer = OrderSerializers(data=order_data)
            if order_serializer.is_valid():
                order_serializer.save()

                # Optionally, you can mark cart items as processed or remove them from the cart
                # cart_items.delete()

                return Response(order_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

