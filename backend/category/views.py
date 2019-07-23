from django.core.serializers import get_serializer
from django.db.models import Q
from rest_framework import generics, status
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
        try:
            data = self.create(request, *args, **kwargs)
        except Exception as e:
            return Response({"result": "fail", "message": str(e), "data": None}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"result": "success", "message": None, "data": data}, status=status.HTTP_201_CREATED)


class CategoryDetailView(mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         mixins.ListModelMixin,
                         generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # def get(self, request, *args, **kwargs):
    #
    #     try:
    #         if 'name' in self.kwargs:
    #             queryset = self.queryset.filter(name=kwargs['name'])  # Category.objects.filter(name=kwargs['name'])
    #             serializer = self.get_serializer(queryset, many=True)
    #             return Response({"result": "success", "message": None, "data": serializer.data})
    #     except Exception as e:
    #         return Response({"result": "fail", "message": str(e), "data": None}, status=status.HTTP_400_BAD_REQUEST)
    #
    #     try:
    #         data = self.retrieve(self, request, *args, **kwargs)
    #     except Exception as e:
    #         return Response({"result": "fail", "message": str(e), "data": None}, status=status.HTTP_400_BAD_REQUEST)
    #     return Response({"result": "success", "message": None, "data": data})

    def put(self, request, *args, **kwargs):
        try:
            data = self.update(request, *args, **kwargs)
        except Exception as e:
            return Response({"result": "fail", "message": None, "data": None}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"result": "success", "message": None, "data": data}, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        try:
            data = self.delete(request, *args, **kwargs)
        except Exception as e:
            return Response({"result": "fail", "message": str(e), "data": None}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"result": "success", "message": None, "data": data}, status=status.HTTP_200_OK)


class CategoryProductView(mixins.RetrieveModelMixin,
                          generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        if 'name' in self.kwargs:
            category = Category.objects.filter(name=kwargs['name'])
            if not len(category):
                return Response({"result": "fail", "message": "", "data": None}, status=status.HTTP_400_BAD_REQUEST)

            queryset = self.queryset.filter(Q(category=category[0].id) | Q(category__parent=category[0].id))
            serializer = self.get_serializer(queryset, many=True)
            return Response({"result": "success", "message": None, "data": serializer.data}, status=status.HTTP_200_OK)

        queryset = self.queryset.filter(Q(category=self.kwargs['pk']) | Q(category__parent=self.kwargs['pk']))
        serializer = self.get_serializer(queryset, many=True)
        return Response({"result": "success", "message": None, "data": serializer.data}, status=status.HTTP_200_OK)
