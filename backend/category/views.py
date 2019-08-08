from django.db.models import Q
from oauth2_provider.views import ProtectedResourceView
from rest_framework import status
from rest_framework.response import Response

from product.models import Product
# from product.serializers import ProductSerializer, ProductSimpleSerializer
from .models import Category
from .serializers import CategorySerializer, CategoryProductSerializer, \
    CategoryPraentProductSerializer, CategoryParentSerializer, ProductSimpleSerializer
from myModule.myGenerics import *


class CategoryLV(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TopCategoryLV(ListAPIView):
    queryset = Category.objects.filter(parent=None)
    serializer_class = CategoryParentSerializer


class CategoryFriendLV(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryParentSerializer

    def get_queryset(self):
        category = self.queryset.filter(pk=self.kwargs['pk'])
        if category[0].parent is None:
            return category
        return self.queryset.filter(pk=category[0].parent.pk)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        data = {
            "child_categorys" : serializer.data,
            "choice_category" : self.queryset.get(pk=self.kwargs['pk']).name
        }
        return Response({"result": "success", "message": None, "data": data}, status=status.HTTP_200_OK)


class CategoryDV(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryNameDV(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'name'
    lookup_url_kwarg = 'name'


class CategoryNameProductLV(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSimpleSerializer

    def get_queryset(self):
        return self.queryset.filter(
            Q(category__name=self.kwargs['name']) | Q(category__parent__name=self.kwargs['name']))


class CategoryProductLV(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSimpleSerializer

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Product.objects.none()

        return self.queryset.filter(Q(category=self.kwargs['pk']) | Q(category__parent=self.kwargs['pk']))
