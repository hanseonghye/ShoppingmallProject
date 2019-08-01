from rest_framework import generics, status
from rest_framework.response import Response

from cart.serializers import CartSerializer, CartsSerializer
from myModule.myGenerics import *
from .models import Cart


class CartLV(mixins.CreateModelMixin,
             ListAPIView,
             generics.GenericAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartsSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.kwargs['pk'])

    def post(self, request, *args, **kwargs):
        try:
            data = self.create(request.data['cart'], many=True, *args, **kwargs)
        except Exception as e:
            return Response({"result": "fail", "message": str(e), "data": None}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"result": "success", "message": None, "data": data}, status=status.HTTP_200_OK)


class CartDV(RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    lookup_url_kwarg = 'cartpk'
