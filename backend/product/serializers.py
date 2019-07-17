from rest_framework import serializers

from category.models import Category
from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    price = serializers.IntegerField()
    category_id = serializers.IntegerField()

    stock = serializers.BooleanField()
    display = serializers.BooleanField()

    file_url = serializers.CharField()
    image_url = serializers.CharField()

    class Meta:
        model = Product
        fields = ('name', 'price', 'category_id', 'stock', 'display', 'file_url', 'image_url')

    def create(self, request):
        product = Product.objects.create(**request)
        product.save()
        return product
