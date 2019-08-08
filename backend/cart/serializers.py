from django.utils import timezone
from rest_framework import serializers

from cart.models import Cart
from category.serializers import ProductSimpleSerializer
from product.serializers import ProductSerializer
from user.serializers import UserSerializer


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('user', 'non_user', 'product', 'product_detail', 'amount')

        extra_kwargs = {
            'user': {'write_only': True},
            'non_user': {'write_only': True}
        }

    def create(self, request):
        cart = Cart.objects.create(expiry_date=timezone.now(), **request)
        return cart


class CartsSerializer(serializers.ModelSerializer):
    # user = UserSerializer(write_only=True)
    # non_user = CartSerializer(write_only=True)

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


class CartProductSerializer(serializers.ModelSerializer):
    product = ProductSimpleSerializer(read_only=True)

    class Meta:
        model = Cart
        fields = ('pk','user','non_user' ,'product', 'product_detail', 'amount')


class CartProductAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('user','non_user' ,'product', 'product_detail', 'amount')
        extra_kwargs = {
            'product': {'required': False},
            'product_detail': {'required': False},
            'user': {'required': False},
            'non_user': {'required': False},
        }

    def create(self, request):

        cart = Cart.objects.create(expiry_date=timezone.now(), **request)
        return cart