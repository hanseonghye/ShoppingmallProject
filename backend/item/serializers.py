from rest_framework import serializers

from item.models import Item


class ItemSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    price = serializers.IntegerField()
    display = serializers.BooleanField()
    stock = serializers.BooleanField()
    file_url = serializers.URLField()
    image_url = serializers.URLField()
    category_id = serializers.IntegerField()

    class Meta:
        model = Item
        fields = ('name', 'price', 'display', 'stock', 'file_url', 'image_url', 'category_id')
