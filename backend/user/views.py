from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer
from .models import CustomUser as User
from myModule import myMixins as mixins


class UserListView(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        data = self.list(request, *args, **kwargs)
        return Response({"result": "success", "message": None, "data": data})

    def post(self, request, *args, **kwargs):
        try:
            data = self.create(request, *args, **kwargs)
        except Exception as e:
            return Response({"result": "fail", "message": str(e), "data": None})

        return Response({"result": "success", "message": None, "data": data})


class UserDetailView(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.ListModelMixin,
                     generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def __init__(self):
        self.data = None

    def get(self, request, *args, **kwargs):
        try:
            data = self.retrieve(self, request, *args, **kwargs)
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


@api_view(['GET'])
def check_id(request, user_id=''):
    result = User.objects.filter(user_id=user_id).exists()
    return Response({"result": "success", "message": None, "data": result})


@api_view(['GET'])
def check_email(request, email=''):
    result = User.objects.filter(email=email).exists()
    return Response({"result": "success", "message": None, "data": result})
