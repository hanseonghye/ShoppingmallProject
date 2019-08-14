from django.utils import timezone
from rest_framework import serializers

from order.models import Order, OrderProduct
from product.serializers import ProductSerializer
from user.models import CustomUser as User
from product.models import Product
from user.serializers import UserSerializer


class OrderProductDetailSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderProduct
        fields = ('order', 'product_detail', 'product', 'amount', 'price', 'all_price')
        extra_kwargs = {
            'product_detail': {'required': False},
            'all_price': {'read_only': True},
            'price': {'read_only': True},
            'product': {'read_only': True},
        }


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ('order', 'product_detail', 'product', 'amount', 'price', 'all_price')
        extra_kwargs = {
            'product_detail': {'required': False},
            'all_price': {'read_only': True},
            'price': {'read_only': True},
        }

    def create(self, request):
        product = Product.objects.get(id=request['product'].id)
        order_product = OrderProduct.objects.create(**request)
        if not Product.objects.get(id=request['product'].id).is_option:
            order_product.price = product.price

        order_product.all_price = order_product.price * order_product.amount
        order_product.date = timezone.now()
        order_product.save()

        order = Order.objects.get(id=order_product.order)
        order.price += order_product.all_price
        if order.status is 0:
            order.status = 1
        order.save()

        return order_product


class OrderListSerializer(serializers.ModelSerializer):
    order_products = OrderProductDetailSerializer(many=True, read_only=True)
    date = serializers.DateTimeField(format="%Y-%m-%d, %H:%M:%S")
    status = serializers.CharField(read_only=True,source='get_status_display')
    pay_type = serializers.CharField(source='get_pay_type_display')

    class Meta:
        model = Order
        fields = ('pk',
                  'user', 'sender_name', 'sender_email', 'sender_phone_number', 'receiver_name',
                  'receiver_phone_number', 'receiver_address', 'delivery_message', 'pay_type', 'date',
                  'order_products', 'status',
                  )
        extra_kwargs = {
            'pk': {'read_only': True},
            'date': {'read_only': True},
        }


class OrderUserSerializer(serializers.ModelSerializer):
    # order_products = OrderProductSerializer(many=True, read_only=True)
    status = serializers.CharField(read_only=True, source='get_status_display')
    user = UserSerializer(read_only=True)
    date = serializers.DateTimeField(format="%Y-%m-%d, %H:%M:%S")

    class Meta:
        model = Order
        fields = ('pk', 'date', 'price','user', 'pay_type','status')


class OrderSerializer(serializers.ModelSerializer):
    order_products = OrderProductSerializer(many=True, read_only=True)
    status = serializers.CharField(read_only=True)

    class Meta:
        model = Order
        fields = (
            'user', 'sender_name', 'sender_email', 'sender_phone_number', 'receiver_name',
            'receiver_phone_number', 'receiver_address', 'delivery_message', 'pay_type',
            'order_products', 'status',
        )

        extra_kwargs = {'user': {'required': False},
                        'sender_name': {'required': False},
                        'sender_email': {'required': False},
                        'sender_phone_number': {'required': False},
                        'status': {'required': False},
                        'delivery_message': {'required': False},
                        # 'order_products': {'required': False}
                        }

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
        order.save()
        return order


class OrdersSerializer(serializers.ModelSerializer):
    order_products = OrderProductSerializer(many=True)
    status = serializers.CharField(read_only=True)

    class Meta:
        model = Order
        fields = (
            'user', 'sender_name', 'sender_email', 'sender_phone_number', 'receiver_name',
            'receiver_phone_number', 'receiver_address', 'delivery_message', 'pay_type', 'status',
            'order_products'
        )

        extra_kwargs = {
            'user': {'required': False, 'write_only': True},
            'sender_name': {'required': False},
            'sender_email': {'required': False},
            'sender_phone_number': {'required': False},
            'status': {'required': False},
            'order_products': {'required': True},
            'price': {'read_only': True}
        }

    def create(self, request):
        order_products = request.pop('order_products')

        if 'user' not in request:  # 비회원
            if not all(x in ['sender_name', 'sender_email', 'sender_phone_number'] for x in request):
                raise serializers.ValidationError("null sender value")

        # if not all(x in ['receiver_name', 'receiver_phone_number', 'receiver_address'] for x in request):
        #     raise serializers.ValidationError("null receiver value")

        order = Order.objects.create(status=0, price=0, **request)
        # for op in order_products:
        #     OrderProduct.objects.create(order=order, **op)
        real_price = 0
        for op in order_products:
            order_product = OrderProduct.objects.create(order=order, **op)
            if op['product'].is_option:
                order_product.price = op['product'].price
            order_product.price = op['product'].price
            order_product.all_price = int(op['product'].price) * int(order_product.amount)
            order_product.date = timezone.now()
            order_product.save()
            real_price += order_product.all_price
        order.price = real_price
        order.status = 1
        order.save()
        return order
