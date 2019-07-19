from rest_framework import serializers

from product.models import Product, Option, OptionDetail, ProductDetail


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'price', 'stock', 'display', 'file_url', 'image_url')

    def create(self, request):
        product = Product.objects.create(**request)
        product.save()
        return product


# class ProductCategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductCategory
#         fields = '__all__'
#
#     def create(self, request):
#         product_category = ProductCategory.objects.create(**request)
#         product_category.save()
#         return product_category


class OptionSerializer(serializers.ModelSerializer):
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
