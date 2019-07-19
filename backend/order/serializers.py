from rest_framework import serializers

from order.models import Order, OrderProduct


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def create(self, request):
        order = Order.objects.crate(**request)
        order.save()
        return order


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = '__all__'

    def create(self, request):
        order_product = OrderProduct.objects.create(**request)
        order_product.save()
        return order_product
