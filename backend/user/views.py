from django.db.models import Q
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from myModule.myGenerics import *
from .serializers import UserSerializer, AddressSerializer
from .models import CustomUser as User, Address
from myModule import myMixins as mixins


class UserLV(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCV(CreateAPIView):
    serializer_class = UserSerializer


# ProtectedResourceView
class UserDV(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserNameDV(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'user_id'
    lookup_url_kwarg = 'user_id'


class UserAddressLV(ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.kwargs['pk'])


class UserAddressNameLV(ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def get_queryset(self):
        return self.queryset.filter(user__user_id=self.kwargs['user_id'])


def id_validator(user_id):
    pass


@api_view(['GET'])
def check_id(request, user_id=''):
    if not id_validator(user_id):
        return Response({"result": "fail", "message": "id양식을 맞춰주세요", "data": None}, status=status.HTTP_400_BAD_REQUEST)
    if not User.objects.filter(user_id=user_id).exists():
        return Response({"result": "fail", "message": "이미 사용하고 있는 id입니다.", "data": None},
                        status=status.HTTP_400_BAD_REQUEST)
    return Response({"result": "success", "message": None, "data": "ok"}, status=status.HTTP_200_OK)


@api_view(['GET'])
def check_email(request, email=''):
    result = User.objects.filter(email=email).exists()
    return Response({"result": "success", "message": None, "data": result})
