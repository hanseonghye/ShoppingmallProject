from django.utils import timezone
from rest_framework import serializers

from cart.models import Cart
from product.serializers import ProductSerializer


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('user', 'non_user', 'product', 'product_detail', 'amount')

    def create(self, request):
        cart = Cart.objects.create(expiry_date=timezone.now(), **request)
        return cart


class CartsSerializer(serializers.ModelSerializer):
    # products = ProductSerializer(read_only=True)

    class Meta:
        model = Cart
        fields = ('user', 'non_user', 'product', 'product_detail', 'amount')
        extra_kwargs = {
            'amount': {'required': False},
            'product_detail': {'required': False},
            'user': {'required': False},
            'non_user': {'required': False},
        }

    def create(self, request):
        cart = Cart.objects.create(expiry_date=timezone.now(), **request)
        return cart
