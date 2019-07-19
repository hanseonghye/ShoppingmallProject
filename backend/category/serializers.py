from rest_framework import serializers

from .models import Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name', 'parent')

    def create(self, request):
        category = Category.objects.create(**request)
        category.save()
        return category
