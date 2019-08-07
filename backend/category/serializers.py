from rest_framework import serializers

from product.serializers import ProductSimpleSerializer
from .models import Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('pk', 'name', 'parent','priority')
        ordering = ['priority',]

    def create(self, request):
        category = Category.objects.create(**request)
        category.save()
        return category

class CategoryProductSerializer(serializers.ModelSerializer):
    category_products = ProductSimpleSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ('name','parent', 'priority','category_products')
        extra_kwargs = {
       }
        ordering = ['priority',]

    def create(self, request):
        category = Category.objects.create(**request)
        category.save()
        return category

class CategoryPraentProductSerializer(serializers.ModelSerializer):
    category_child = CategoryProductSerializer(many=True, read_only=True)
    category_products = ProductSimpleSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ('name','parent', 'priority','category_child','category_products')
        extra_kwargs = {
       }
        ordering = ['priority',]

class CategoryParentSerializer(serializers.ModelSerializer):
    category_child = CategorySerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ('pk', 'name','parent', 'priority','category_child')
        extra_kwargs = {
            'pk': {'read_only': True},
       }
        ordering = ['priority',]


