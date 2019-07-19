from rest_framework import serializers

from category.serializers import CategorySerializer
from product.models import Product, Option, OptionDetail, ProductDetail, ProductCategory


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'price', 'stock', 'display', 'file_url', 'image_url')

    def create(self, request):
        product = Product.objects.create(**request)
        product.save()
        return product


class ProductCategorySerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=False)

    class Meta:
        model = ProductCategory
        fields = '__all__'

    def create(self, request):
        product_data = dict(request.pop('product'))
        product = Product.objects.create(**product_data)
        product.save()
        product_category_data = {'product': product, 'category': request['category']}
        product_category = ProductCategory.objects.create(**product_category_data)
        product_category.save()
        return product_category


class OptionSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=False)

    class Meta:
        model = Option
        fields = ('name', 'product')

    def create(self, request):
        option = Option.objects.create(**request)
        option.save()
        return option


class OptionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionDetail
        fields = '__all__'
        # fields = ('name','option')

    def create(self, request):
        option_detail = OptionDetail.objects.create(**request)
        option_detail.save()
        return option_detail


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetail
        fields = '__all__'

    def create(self, request):
        product_dateil = ProductDetail.objects.create(**request)
        product_dateil.save()
        return product_dateil
