from rest_framework import generics, status
from rest_framework.response import Response

from myModule import myMixins as mixins
from myModule.myGenerics import *
from order.models import Order
from order.serializers import OrderSerializer, OrdersSerializer


class OrderLV(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class UserOrderUV(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class UserOrderRV(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'orderpk'


class OrderManyCV(CreateAPIView):
    serializer_class = OrdersSerializer


# class OrderProductAddView(mixins.CreateModelMixin,
#                           mixins.ListModelMixin,
#                           generics.GenericAPIView):
#     queryset = OrderProduct.objects.all()
#     serializer_class = OrderProductSerializer
#
#     # def get(self, request, *args, **kwargs):
#     #     data = self.list(request, *args, **kwargs)
#     #     return Response({"result": "success", "message": None, "data": data})
#
#     def post(self, request, *args, **kwargs):
#         try:
#             data = self.create(request, *args, **kwargs)
#         except Exception as e:
#             return Response({"result": "fail", "message": str(e), "data": None}, status=status.HTTP_400_BAD_REQUEST)
#         return Response({"result": "success", "message": None, "data": data}, status=status.HTTP_200_OK)


class UserOrderLV(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.kwargs['pk'])


class UserOrderNameLV(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        return self.queryset.filter(user__user_id=self.kwargs['user_id'], )
