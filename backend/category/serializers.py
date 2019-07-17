from rest_framework import serializers

from category.models import Category


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    parent_id = serializers.IntegerField(default=None)

    class Meta:
        model = Category
        fields = ('name', 'parent_id')

    def create(self, request):
        category = Category.objects.create(**request)
        category.save()
        return category
