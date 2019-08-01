from django.db.models import Q
from product.models import Product
from product.serializers import ProductSerializer
from .models import Category
from .serializers import CategorySerializer
from myModule.myGenerics import *


class CategoryLV(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDV(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'name'
    lookup_url_kwarg = 'name'


class CategoryNameDV(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'name'
    lookup_url_kwarg = 'name'


class CategoryNameProductLV(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        return self.queryset.filter(
            Q(category__name=self.kwargs['name']) | Q(category__parent__name=self.kwargs['name']))


class CategoryProductLV(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return Product.objects.none()

        return self.queryset.filter(Q(category=self.kwargs['pk']) | Q(category__parent=self.kwargs['pk']))
