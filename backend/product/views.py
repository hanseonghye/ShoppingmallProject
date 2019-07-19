from rest_framework import generics
from rest_framework.response import Response

from product.models import Product, Option, OptionDetail, ProductDetail
from product.serializers import ProductSerializer, OptionSerializer, OptionDetailSerializer, ProductDetailSerializer
from myModule import myMixins as mixins


class ProductListView(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        data = self.list(request, *args, **kwargs)
        return Response({"result": "success", "message": None, "data": data})

    def post(self, request, *args, **kwargs):
        data = self.create(request, *args, **kwargs)
        return Response({"result": "success", "message": None, "data": data})


class ProductDetailView(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.ListModelMixin,
                        generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        data = self.list(request, *args, **kwargs)
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


# class ProductCategoryListView(mixins.CreateModelMixin,
#                               mixins.ListModelMixin,
#                               generics.GenericAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
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
# class ProductCategoryDetailView(mixins.RetrieveModelMixin,
#                                 mixins.UpdateModelMixin,
#                                 mixins.DestroyModelMixin,
#                                 mixins.ListModelMixin,
#                                 generics.GenericAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#     def get(self, request, *args, **kwargs):
#         data = self.list(request, *args, **kwargs)
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


class OptionListView(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     generics.GenericAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer

    def get(self, request, *args, **kwargs):
        data = self.list(request, *args, **kwargs)
        return Response({"result": "success", "message": None, "data": data})

    def post(self, request, *args, **kwargs):
        data = self.create(request, *args, **kwargs)
        return Response({"result": "success", "message": None, "data": data})


class OptionDetailView(mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       mixins.ListModelMixin,
                       generics.GenericAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer

    def get(self, request, *args, **kwargs):
        data = self.list(request, *args, **kwargs)
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


class ProductOptionListView(mixins.CreateModelMixin,
                            mixins.ListModelMixin,
                            generics.GenericAPIView):
    # queryset = Option.objects.all()
    serializer_class = OptionSerializer

    def get_queryset(self):
        if 'pk' in self.kwargs:
            return Option.objects.filter(product_id=self.kwargs['pk'])
        return Option.objects.none()

    def get(self, request, *args, **kwargs):
        data = self.list(request, *args, **kwargs)
        return Response({"result": "success", "message": None, "data": data})

    def post(self, request, *args, **kwargs):
        data = self.create(request, *args, **kwargs)
        return Response({"result": "success", "message": None, "data": data})


class OptionDetailListlView(mixins.CreateModelMixin,
                            mixins.ListModelMixin,
                            generics.GenericAPIView):
    queryset = OptionDetail.objects.all()
    serializer_class = OptionDetailSerializer

    def get(self, request, *args, **kwargs):
        data = self.list(request, *args, **kwargs)
        return Response({"result": "success", "message": None, "data": data})

    def post(self, request, *args, **kwargs):
        data = self.create(request, *args, **kwargs)
        return Response({"result": "success", "message": None, "data": data})


class OptionDetailDetailView(mixins.RetrieveModelMixin,
                             mixins.UpdateModelMixin,
                             mixins.DestroyModelMixin,
                             mixins.ListModelMixin,
                             generics.GenericAPIView):
    queryset = OptionDetail.objects.all()
    serializer_class = OptionDetailSerializer

    def get(self, request, *args, **kwargs):
        data = self.list(request, *args, **kwargs)
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


class OptionDetailListView(mixins.CreateModelMixin,
                           mixins.ListModelMixin,
                           generics.GenericAPIView):
    queryset = ProductDetail.objects.all()
    serializer_class = ProductDetailSerializer

    def get(self, request, *args, **kwargs):
        data = self.list(request, *args, **kwargs)
        return Response({"result": "success", "message": None, "data": data})

    def post(self, request, *args, **kwargs):
        data = self.create(request, *args, **kwargs)
        return Response({"result": "success", "message": None, "data": data})


class OptionDetailDetailView(mixins.RetrieveModelMixin,
                             mixins.UpdateModelMixin,
                             mixins.DestroyModelMixin,
                             mixins.ListModelMixin,
                             generics.GenericAPIView):
    queryset = ProductDetail.objects.all()
    serializer_class = ProductDetailSerializer

    def get(self, request, *args, **kwargs):
        data = self.list(request, *args, **kwargs)
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
