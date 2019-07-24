from rest_framework import generics, status
from rest_framework.response import Response

from myModule import myMixins as mixins
from order.models import Order, OrderProduct, Cart
from order.serializers import OrderSerializer, OrderProductSerializer, CartSerializer


class OrderListView(mixins.ListModelMixin,
                    generics.GenericAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self, request, *args, **kwargs):
        data = self.list(request, *args, **kwargs)
        return Response({"result": "success", "message": None, "data": data})


class OrderDetailView(mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      generics.GenericAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        if 'pk' in self.kwargs:
            return self.queryset.filter(id=self.kwargs['pk'])
        return self.queryset.none()

    # def get(self, request, *args, **kwargs):
    #     try:
    #         data = self.list(request, *args, **kwargs)
    #     except Exception as e:
    #         return Response({"result": "fail", "message": str(e), "data": None})
    #     return Response({"result": "success", "message": None, "data": data})

    def put(self, request, *args, **kwargs):
        try:
            data = self.update(request, *args, **kwargs)
        except Exception as e:
            return Response({"result": "fail", "message": None, "data": None}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"result": "success", "message": None, "data": data}, status=status.HTTP_200_OK)


class OrderAddView(mixins.CreateModelMixin,
                   generics.GenericAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def post(self, request, *args, **kwargs):

        if not isinstance(request.data, list):
            try:
                data = self.create(request, *args, **kwargs)
            except Exception as e:
                return Response({"result": "fail", "message": str(e), "data": None}, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                serializer = self.get_serializer(data=request.data, many=True)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                data = serializer.data
            except Exception as e:
                return Response({"result": "fail", "message": str(e), "data": None}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"result": "success", "message": None, "data": data}, status=status.HTTP_200_OK)


class OrderProductAddView(mixins.CreateModelMixin,
                          mixins.ListModelMixin,
                          generics.GenericAPIView):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer

    # def get(self, request, *args, **kwargs):
    #     data = self.list(request, *args, **kwargs)
    #     return Response({"result": "success", "message": None, "data": data})

    def post(self, request, *args, **kwargs):
        try:
            data = self.create(request, *args, **kwargs)
        except Exception as e:
            return Response({"result": "fail", "message": str(e), "data": None}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"result": "success", "message": None, "data": data}, status=status.HTTP_200_OK)


class OrderProductListView(mixins.CreateModelMixin,
                           mixins.ListModelMixin,
                           generics.GenericAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        if 'user_id' in self.kwargs:
            return self.queryset.filter(user__user_id=self.kwargs['user_id'], )
            # return self.queryset.exclude(status=0).filter(user__user_id=self.kwargs['user_id'], )

        if 'pk' in self.kwargs:
            return self.queryset.filter(user=self.kwargs['pk'])
            # return self.queryset.exclude(status=0).filter(user=self.kwargs['pk'])
        return None

    def get(self, request, *args, **kwargs):
        try:
            data = self.list(request, *args, **kwargs)
        except Exception as e:
            return Response({"result": "fail", "message": str(e), "data": None})
        return Response({"result": "success", "message": None, "data": data})

    def post(self, request, *args, **kwargs):
        try:
            data = self.create(request, *args, **kwargs)
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


class CartListView(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   generics.GenericAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

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
            data = self.create(request, *args, **kwargs)
        except Exception as e:
            return Response({"result": "fail", "message": str(e), "data": None}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"result": "success", "message": None, "data": data}, status=status.HTTP_200_OK)


class CartDetailView(mixins.DestroyModelMixin,
                     mixins.UpdateModelMixin,
                     generics.GenericAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get_queryset(self):
        if 'cartpk' in self.kwargs:
            return self.queryset.get(id=self.kwargs['cartpk'])
        return self.queryset.none()

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
