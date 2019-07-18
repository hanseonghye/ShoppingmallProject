from rest_framework import mixins, generics
from rest_framework.response import Response

from product.models import Product
from product.serializers import ProductSerializer


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
        data = self.retrieve(request, *args, **kwargs)
        return Response({"result": "success", "message": None, "data": data})

    def delete(self, request, *args, **kwargs):
        data = self.delete(request, *args, **kwargs)
        return Response({"result": "success", "message": None, "data": data})
