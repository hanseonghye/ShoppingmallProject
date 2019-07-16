from rest_framework import viewsets

from .models import Category
from .serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        if 'id' in self.kwargs:
            queryset = Category.objects.filter(id=self.kwargs['id'])
        elif 'name' in self.kwargs:
            queryset = Category.objects.filter(name=self.kwargs['name'])
        else:
            queryset = Category.objects.all()

        return queryset
