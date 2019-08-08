from rest_framework import generics, status
from rest_framework.response import Response

from cart.serializers import CartSerializer, CartsSerializer, CartProductSerializer, CartProductAddSerializer
from myModule.myGenerics import *
from .models import Cart


class CartLV(ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartProductSerializer

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return Cart.objects.none()

        return self.queryset.filter(user=self.kwargs['pk'])

class CartCV(CreateAPIView):
    serializer_class = CartProductAddSerializer


class CartDV(RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    lookup_url_kwarg = 'cartpk'


class NonUserCartLV(ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartProductSerializer

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return Cart.objects.none()

        return self.queryset.filter(non_user=self.kwargs['pk'])


class NonUserCartDV(RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    lookup_url_kwarg = 'cartpk'
