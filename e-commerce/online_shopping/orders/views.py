# from django.shortcuts import render
# from django.db import transaction

# from rest_framework.views import APIView

# from .models import Order
# from user.models import CustomUser
# from products.models import Product
# from shopping_cart.models import CartItem

# from .serializers import OrderSerializers
# from rest_framework import status
# from rest_framework.response import Response
# from django.http import Http404
# from decimal import Decimal 


# class CheckoutView(APIView):
#     def post(self,request):
#         user = request.user

#         shipping_address = request.data.get('shipping_address', '')
#         cart_item_ids = request.data.get('cart_item', [])
#         print(cart_item_ids)
#         print(shipping_address)


#         # cart = CartItem.objects.filter(user=user)
#         # total_amount = Decimal('0.00')
#         # for items in cart:
#         #     product = items.product #items.product_id
#         #     quantity = items.quantity
#         #     # pid = Product.objects.get(id=product)
#         #     # price = pid.price

#         #     subtotal = product.price * quantity
#         #     total_amount += subtotal


#         total_amount = Decimal('0.00')
#         for cart_item_id in cart_item_ids:
#             cart_item = CartItem.objects.get(pk=cart_item_id)
#             subtotal = cart_item.product.price * cart_item.quantity
#             total_amount += subtotal

#         print(total_amount, user.id)

#         # order_data = {
#         #     'user': user.id, 
#         #     'total_amount': total_amount,
#         #     'shipping_address': shipping_address, 
#         # }


#         with transaction.atomic():
#             order_serializer = OrderSerializers(data=request.data)
            
#             if order_serializer.is_valid():
#                 cart_item = order_serializer.validated_data['cart_item']
#                 order_serializer.validated_data['total_amount'] = total_amount

#                 order = order_serializer.save()
                

#                 # order.calculate_total_amount()

#                 # Add cart items to the order
#                 # for cart_item_id in cart_item_ids:
#                 #     order.cart_item.get(cart_item_id)

#                 return Response(order_serializer.data, status=status.HTTP_201_CREATED)
#             else:
#                 return Response(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

