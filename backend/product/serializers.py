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


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ('name', 'product')

    def create(self, request):
        option = Option.objects.create(**request)
        option.save()
        return option


class OptionDetailSerializer(serializers.ModelSerializer):
    # option = OptionSerializer(read_only=True)

    class Meta:
        model = OptionDetail
        fields = ('pk','name', 'option')
        extra_kwargs = {
            'option': {'required': False}
        }

    def create(self, request):
        option_detail = OptionDetail.objects.create(**request)
        option_detail.save()
        return option_detail


class OptionsSerializer(serializers.ModelSerializer):
    option_details = OptionDetailSerializer(many=True)

    class Meta:
        model = Option
        fields = ('pk', 'name', 'product', 'option_details')

        extra_kwargs = {
            'product': {'required': False},
            'option_details': {'required': False},
        }

    def create(self, request):
        option = Option.objects.create(**request)
        option.save()
        return option


class ProductAdminSerializer(serializers.ModelSerializer):
    product_details = ProductDetailSerializer(many=True, read_only=True)
    product_options = OptionsSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = (
            'name', 'price', 'is_stock', 'is_display', 'is_option', 'file_url', 'image_url', 'category',
            'product_details',
            'product_options')

class AddProductSerializer(serializers.ModelSerializer):
    product_options = OptionsSerializer(many=True)

    class Meta:
        model = Product
        fields = (
            'name', 'price', 'is_stock', 'is_display', 'is_option', 'file_url', 'image_url', 'category','description',
            'product_options')

        extra_kwargs = {
            'product_options': {'required': False}
        }

    def create(self, request):
        options = request.pop('product_options')

        product = Product.objects.create(**request)
        for option in options:
            option_details = option.pop("option_details")
            o = Option.objects.create(product=product, **option)
            for option_detail in option_details:
                OptionDetail.objects.create(option=o, **option_detail)

        return product

class ProductSerializer(serializers.ModelSerializer):
    product_details = ProductDetailSerializer(many=True, read_only=True)
    product_options = OptionsSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = (
            'pk','name', 'price', 'is_stock', 'is_display', 'is_option', 'file_url', 'image_url', 'category','description',
            'product_details', 'product_options')

        extra_kwargs = {
            'pk': {'read_only': False}
        }

    def create(self, request):
        product = Product.objects.create(**request)
        return product