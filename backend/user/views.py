from django.db.models import Q
from oauth2_provider.views.generic import ProtectedResourceView
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from backend.permissions import IsAuthenticatedOrCreate
from .serializers import UserSerializer, AddressSerializer
from .models import CustomUser as User, Address
from myModule import myMixins as mixins


class UserListView(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        data = self.list(request, *args, **kwargs)
        return Response({"result": "success", "message": None, "data": data})


class UserAddView(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (IsAuthenticatedOrCreate,)

    def post(self, request, *args, **kwargs):
        try:
            data = self.create(request, *args, **kwargs)
        except Exception as e:
            return Response({"result": "fail", "message": str(e), "data": None}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"result": "success", "message": None, "data": data}, status=status.HTTP_201_CREATED)


# ProtectedResourceView
class UserDetailView(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.ListModelMixin,
                     generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        try:
            if 'user_id' in self.kwargs:
                queryset = self.queryset.filter(user_id=kwargs['user_id'])
                serializer = self.get_serializer(queryset, many=True)
                data = serializer.data
            else:
                data = self.retrieve(self, request, *args, **kwargs)
        except Exception as e:
            return Response({"result": "fail", "message": str(e), "data": None}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"result": "success", "message": None, "data": data}, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        try:
            data = self.update(self, request, *args, **kwargs)
        except Exception as e:
            return Response({"result": "fail", "message": str(e), "data": None}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"result": "success", "message": None, "data": data}, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        try:
            self.destroy(self, request, *args, **kwargs)
        except Exception:
            return Response({"result": "fail", "message": None, "data": None}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"result": "success", "message": None, "data": "ok"}, status=status.HTTP_200_OK)


class UserAddressListView(mixins.CreateModelMixin,
                          mixins.ListModelMixin,
                          generics.GenericAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def get(self, request, *args, **kwargs):
        try:

            if 'user_id' in self.kwargs:
                queryset = self.queryset.filter(user__user_id=kwargs['user_id'])
                serializer = self.get_serializer(queryset, many=True)
                data = serializer.data
            else:
                queryset = self.queryset.filter(user=kwargs['pk'])
                serializer = self.get_serializer(queryset, many=True)
                data = serializer.data
        except Exception as e:
            return Response({"result": "fail", "message": str(e), "data": None})
        return Response({"result": "success", "message": None, "data": data})

    def post(self, request, *args, **kwargs):
        try:
            data = self.create(request, *args, **kwargs)
        except Exception as e:
            return Response({"result": "fail", "message": str(e), "data": None}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"result": "success", "message": None, "data": data}, status=status.HTTP_201_CREATED)


class UserAddressDetailView(mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            generics.GenericAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def get(self, request, *args, **kwargs):
        try:
            if 'user_id' in self.kwargs:
                queryset = self.queryset.filter(Q(user__user_id=kwargs['user_id']))
                serializer = self.get_serializer(queryset, many=True)
                data = serializer.data
            else:
                queryset = self.queryset.filter(user=kwargs['pk'])
                serializer = self.get_serializer(queryset, many=True)
                data = serializer.data
        except Exception as e:
            return Response({"result": "fail", "message": str(e), "data": None})
        return Response({"result": "success", "message": None, "data": data})

    def post(self, request, *args, **kwargs):
        try:
            data = self.create(request, *args, **kwargs)
        except Exception as e:
            return Response({"result": "fail", "message": str(e), "data": None})

        return Response({"result": "success", "message": None, "data": data})

    def put(self, request, *args, **kwargs):
        try:
            data = self.update(request, *args, **kwargs)
        except Exception as e:
            return Response({"result": "fail", "message": str(e), "data": None})
        return Response({"result": "success", "message": None, "data": data})

    def delete(self, request, *args, **kwargs):
        try:
            self.destroy(self, request, *args, **kwargs)
        except Exception:
            return Response({"result": "fail", "message": None, "data": None})
        return Response({"result": "success", "message": None, "data": "ok"})


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
