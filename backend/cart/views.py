from rest_framework import generics, status
from rest_framework.response import Response

from cart.serializers import CartSerializer, CartsSerializer
from myModule import myMixins as mixins
from .models import Cart


class CartListView(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   generics.GenericAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartsSerializer

    def get_queryset(self):
        if 'pk' in self.kwargs:
            return self.queryset.filter(user=self.kwargs['pk'])
        return self.queryset.none()

    def get(self, request, *args, **kwargs):
        try:
            data = self.list(request, *args, **kwargs)
        except Exception as e:
            return Response({"result": "fail", "message": str(e), "data": None})
        return Response({"result": "success", "message": None, "data": data})

    def post(self, request, *args, **kwargs):
        try:
            data = self.create(request.data['cart'], many=True, *args, **kwargs)
        except Exception as e:
            return Response({"result": "fail", "message": str(e), "data": None}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"result": "success", "message": None, "data": data}, status=status.HTTP_200_OK)


class CartDetailView(mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.UpdateModelMixin,
                     generics.GenericAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    lookup_url_kwarg = 'cartpk'

    def get(self, reuqest, *args, **kwargs):
        try:
            data = self.retrieve(reuqest, *args, **kwargs)
        except Exception as e :
            return Response({"result": "success", "message": str(e), "data": None})
        return Response({"result": "success", "message": None, "data": data})

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

# class CartAddView(mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Cart.objects.all()
#     serializer_class = CartSerializer
#
#     def post(self, request, *args, **kwargs):
#         try:
#             data = self.create(request, *args, **kwargs)
#         except Exception as e:
#             return Response({"result": "fail", "message": str(e), "data": None}, status=status.HTTP_400_BAD_REQUEST)
#         return Response({"result": "success", "message": None, "data": data}, status=status.HTTP_200_OK)
