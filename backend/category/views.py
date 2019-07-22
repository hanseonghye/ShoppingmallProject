from django.core.serializers import get_serializer
from django.db.models import Q
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from product.models import Product
from product.serializers import ProductSerializer
from .models import Category
from .serializers import CategorySerializer
from myModule import myMixins as mixins


class CategoryListView(mixins.CreateModelMixin,
                       mixins.ListModelMixin,
                       generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        data = self.list(request, *args, **kwargs)
        return Response({"result": "success", "message": None, "data": data})

    def post(self, request, *args, **kwargs):
        data = self.create(request, *args, **kwargs)
        return Response({"result": "success", "message": None, "data": data})


class CategoryDetailView(mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         mixins.ListModelMixin,
                         generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):

        if 'name' in self.kwargs:
            queryset = self.queryset.filter(name=kwargs['name'])  # Category.objects.filter(name=kwargs['name'])
            serializer = self.get_serializer(queryset, many=True)
            return Response({"result": "success", "message": None, "data": serializer.data})

        data = self.retrieve(self, request, *args, **kwargs)
        return Response({"result": "success", "message": None, "data": data})

    def put(self, request, *args, **kwargs):
        try:
            data = self.update(request, *args, **kwargs)
        except Exception as e:
            return Response({"result": "fail", "message": None, "data": None})
        return Response({"result": "success", "message": None, "data": data})

    def delete(self, request, *args, **kwargs):
        data = self.delete(request, *args, **kwargs)
        return Response({"result": "success", "message": None, "data": data})


class CategoryProductView(mixins.RetrieveModelMixin,
                          generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        if 'name' in self.kwargs:
            category = Category.objects.filter(name=kwargs['name'])
            if not len(category):
                return Response({"result": "fail", "message": "", "data": None})

            queryset = self.queryset.filter(Q(category=category[0].id) | Q(category__parent=category[0].id))
            serializer = self.get_serializer(queryset, many=True)
            return Response({"result": "success", "message": None, "data": serializer.data})

        queryset = self.queryset.filter(Q(category=self.kwargs['pk']) | Q(category__parent=self.kwargs['pk']))
        serializer = self.get_serializer(queryset, many=True)
        return Response({"result": "success", "message": None, "data": serializer.data})
