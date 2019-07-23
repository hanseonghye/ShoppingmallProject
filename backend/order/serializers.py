from django.utils import timezone
from rest_framework import serializers

from order.models import Order, OrderProduct, Cart
from product.models import Product


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('user', 'username', 'phone_number', 'address', 'address_detail', 'delivery_message', 'pay_type')

    def create(self, request):
        order = Order.objects.create(**request)
        order.save()
        return order


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = '__all__'

    def create(self, request):
        product = Product.objects.get(id=request['product'].id)
        order_product = OrderProduct.objects.create(**request)
        if Product.objects.get(id=request['product'].id).is_option:
            order_product.price = 1
        else:
            order_product.price = product.price
        order_product.all_price = order_product.price * order_product.count
        order_product.date = timezone.now()
        order_product.save()
        return order_product


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('user', 'non_user', 'product', 'product_detail', 'amount')

    def create(self, request):
        cart = Cart.objects.create(**request)
        cart.expiry_date = timezone.now()
        cart.save()
        return cart
