from django.utils import timezone
from rest_framework import serializers

from order.models import Order, OrderProduct, Cart
from product.models import Product


class OrderProductSerializer(serializers.ModelSerializer):
    # order = OrderSerializer(source='order')

    class Meta:
        model = OrderProduct
        fields = ('order', 'product_detail', 'product', 'amount', 'price')
        extra_kwargs = {
            'product_detail': {'required': False},
        }
        # depth = 0

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

        order = Order.objects.get(id=order_product.order)
        order.price += order_product.all_price
        if order.status is 0:
            order.status = 1
        order.save()

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


class OrderSerializer(serializers.ModelSerializer):
    order_products = OrderProductSerializer(many=True, read_only=True)
    status = serializers.CharField(read_only=True)
    class Meta:
        model = Order
        fields = (
            'user', 'sender_name', 'sender_email', 'sender_phone_number', 'receiver_name',
            'receiver_phone_number', 'receiver_address', 'delivery_message', 'pay_type',
            'order_products','status',
        )

        extra_kwargs = {'user': {'required': False}, 'sender_name': {'required': False},
                        'sender_email': {'required': False}, 'sender_phone_number': {'required': False}}

    def create(self, request):
        order = Order.objects.create(**request)
        if request['user'] is None:  # 비회원
            order.user = None
            if request['sender_name'] is None or request['sender_email'] is None \
                    or request['sender_phone_number'] is None:
                raise serializers.ValidationError("null sender value")
        if request['receiver_name'] is None or request['receiver_phone_number'] is None \
                or request['receiver_address'] is None:
            raise serializers.ValidationError("null receiver value")
        order.status = 0
        order.price = 0
        order = Order.objects.create(**request)
        order.save()
        return order
