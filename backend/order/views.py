from myModule.myGenerics import *
from order.models import Order
from order.serializers import OrderSerializer, OrdersSerializer, OrderListSerializer, OrderUserSerializer


class OrderLV(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderUserSerializer


class UserOrderUV(RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer


class UserOrderRV(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'orderpk'


class OrderManyCV(CreateAPIView):
    serializer_class = OrdersSerializer


class UserOrderLV(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return Order.objects.none()
        return self.queryset.filter(user=self.kwargs['pk'])


class UserOrderNameLV(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer

    def get_queryset(self):
        return self.queryset.filter(user__user_id=self.kwargs['user_id'], )


class NoneUserOrderRV(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        return self.queryset.filter(non_user = self.kwargs['nonuser_id'])
