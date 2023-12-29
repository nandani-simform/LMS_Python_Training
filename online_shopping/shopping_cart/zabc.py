
class CartItem(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # class Meta:
    #     unique_together = ('user', 'product')

    def __str__(self):
        return self.product
    

class CartItem(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product, through='Cart')  

    def __str__(self):
        return f"Cart for {self.user.username}"

    def total_price(self):
        return sum(item.product.price * item.quantity for item in self.cartitem_set.all())

class Cart(models.Model):
    usercart = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} * {self.product.product_name} in {self.usercart.username}'s cart"
    




# def post(self, request):
    #     serializer = CartSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()  # Save the data to the Cart model
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request):
        user = request.user
        print(user)
        product_id = request.data.get('product') 
        quantity = request.data.get('quantity', 1)


        print(product_id)
        cart, created   = Cart.objects.get_or_create(usercart=user,product=product_id)
        print(cart)
        # cart_item, item_created = cart.cart_items.get_or_created(product=product_id)
        # print(cart_item.quantity)

        # if not item_created:
        #     cart_item.quantity += int(quantity)
        #     cart_item.save()

        serializer = CartSerializer(cart)  # Serialize the entire cart
        return Response(serializer.data, status=status.HTTP_201_CREATED)