from django.db.models import Q
from rest_framework import generics, status
from rest_framework.response import Response

from myModule.myGenerics import *
from product.models import Product, Option, OptionDetail, ProductDetail
from .serializers import *
from myModule import myMixins as mixins


class ProductCV(CreateAPIView):
    serializer_class = ProductSerializer


class ProductDV(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRV(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OptionLV(ListCreateAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionsSerializer

    def get_queryset(self):
        if 'pk' in self.kwargs:
            return self.queryset.filter(product=self.kwargs['pk'])
        return self.queryset.none()


class OptionDV(RetrieveUpdateDestroyAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionsSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'optionpk'


class OptionDetailLV(ListCreateAPIView):
    queryset = OptionDetail.objects.all()
    serializer_class = OptionDetailSerializer

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return OptionDetail.objects.none()
        return self.queryset.filter(option=self.kwargs['optionpk'])


class OptionDetailDV(RetrieveUpdateDestroyAPIView):
    queryset = OptionDetail.objects.all()
    serializer_class = OptionDetailSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'detailpk'

# class OptionDetailListlView(mixins.CreateModelMixin,
#                             mixins.ListModelMixin,
#                             generics.GenericAPIView):
#     queryset = OptionDetail.objects.all()
#     serializer_class = OptionDetailSerializer
#
#     def get(self, request, *args, **kwargs):
#         data = self.list(request, *args, **kwargs)
#         return Response({"result": "success", "message": None, "data": data})
#
#     def post(self, request, *args, **kwargs):
#         data = self.create(request, *args, **kwargs)
#         return Response({"result": "success", "message": None, "data": data})
#
#
# class OptionDetailDetailView(mixins.RetrieveModelMixin,
#                              mixins.UpdateModelMixin,
#                              mixins.DestroyModelMixin,
#                              mixins.ListModelMixin,
#                              generics.GenericAPIView):
#     queryset = OptionDetail.objects.all()
#     serializer_class = OptionDetailSerializer
#
#     def get(self, request, *args, **kwargs):
#         data = self.retrieve(request, *args, **kwargs)
#         return Response({"result": "success", "message": None, "data": data})
#
#     def put(self, request, *args, **kwargs):
#         try:
#             data = self.update(request, *args, **kwargs)
#         except Exception as e:
#             return Response({"result": "fail", "message": None, "data": None})
#         return Response({"result": "success", "message": None, "data": data})
#
#     def delete(self, request, *args, **kwargs):
#         data = self.delete(request, *args, **kwargs)
#         return Response({"result": "success", "message": None, "data": data})

# class ProductDetailListView(mixins.CreateModelMixin,
#                             mixins.ListModelMixin,
#                             generics.GenericAPIView):
#     queryset = ProductDetail.objects.all()
#     serializer_class = ProductDetailSerializer
#
#     def get(self, request, *args, **kwargs):
#         data = self.list(request, *args, **kwargs)
#         return Response({"result": "success", "message": None, "data": data})
#
#     def post(self, request, *args, **kwargs):
#         data = self.create(request, *args, **kwargs)
#         return Response({"result": "success", "message": None, "data": data})
#
#
# class ProductDetailDetailView(mixins.RetrieveModelMixin,
#                               mixins.UpdateModelMixin,
#                               mixins.DestroyModelMixin,
#                               mixins.ListModelMixin,
#                               generics.GenericAPIView):
#     queryset = ProductDetail.objects.all()
#     serializer_class = ProductDetailSerializer
#
#     def get(self, request, *args, **kwargs):
#         data = self.retrieve(request, *args, **kwargs)
#         return Response({"result": "success", "message": None, "data": data})
#
#     def put(self, request, *args, **kwargs):
#         try:
#             data = self.update(request, *args, **kwargs)
#         except Exception as e:
#             return Response({"result": "fail", "message": None, "data": None})
#         return Response({"result": "success", "message": None, "data": data})
#
#     def delete(self, request, *args, **kwargs):
#         data = self.delete(request, *args, **kwargs)
#         return Response({"result": "success", "message": None, "data": data})
