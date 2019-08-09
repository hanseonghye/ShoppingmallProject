from rest_framework import serializers

from cart.models import Cart
from product.models import Product
from .models import Category

class CategoryParentSerializer2(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('pk', 'name', 'parent', 'priority')
        ordering = ['priority', ]

class CategorySerializer(serializers.ModelSerializer):
    parent= CategoryParentSerializer2()
    class Meta:
        model = Category
        fields = ('pk', 'name', 'parent', 'priority')
        ordering = ['priority', ]

    def create(self, request):
        category = Category.objects.create(**request)
        if category.parent is not None :
            category.priority = category.parent.priority
        category.save()
        return category


class CategoryParentSerializer(serializers.ModelSerializer):
    category_child = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('pk', 'name', 'parent', 'priority', 'category_child')
        extra_kwargs = {
            'pk': {'read_only': True},
        }
        ordering = ['priority', ]


class ProductSimpleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = (
            'pk', 'name', 'price', 'file_url', 'image_url', 'category')

        extra_kwargs = {
        }


class CategoryProductSerializer(serializers.ModelSerializer):
    category_products = ProductSimpleSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('name', 'parent', 'priority', 'category_products')
        extra_kwargs = {
        }
        ordering = ['priority', ]

    def create(self, request):
        category = Category.objects.create(**request)
        category.save()
        return category


class CategoryPraentProductSerializer(serializers.ModelSerializer):
    category_child = CategoryProductSerializer(many=True, read_only=True)
    category_products = ProductSimpleSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('name', 'parent', 'priority', 'category_child', 'category_products')
        extra_kwargs = {
        }
        ordering = ['priority', ]
