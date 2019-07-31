from rest_framework import serializers

from product.models import Product, Option, OptionDetail, ProductDetail


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetail
        fields = '__all__'

        extra_kwargs = {
            'id': {'required': False},
            'product': {'required': False},
        }


    def create(self, request):
        product_dateil = ProductDetail.objects.create(**request)
        product_dateil.save()
        return product_dateil


class ProductSerializer(serializers.ModelSerializer):
    product_details = ProductDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = (
            'name', 'price', 'is_stock', 'is_display', 'is_option', 'file_url', 'image_url', 'category',
            'product_details')

        extra_kwargs = {
            'is_option': {'write_only': True},
            'is_display': {'write_only': True},
        }

    def create(self, request):
        product = Product.objects.create(**request)
        product.save()
        return product


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
        fields = ('name', 'option')

    def create(self, request):
        option_detail = OptionDetail.objects.create(**request)
        option_detail.save()
        return option_detail


class OptionsSerializer(serializers.ModelSerializer):
    options_detail = OptionDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Option
        fields = ('name', 'product', 'options_detail')

    def create(self, request):
        option = Option.objects.create(**request)
        option.save()
        return option
