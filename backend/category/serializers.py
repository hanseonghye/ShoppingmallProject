from rest_framework import serializers

from .models import Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name', 'parent','order')
        ordering = ['order',]

    def create(self, request):
        category = Category.objects.create(**request)
        category.save()
        return category
