from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import ManagerUserSerializer
from myModule import myMixins as mixins
from user.models import CustomUser as User


class ManagerUserListView(mixins.CreateModelMixin,
                          mixins.ListModelMixin,
                          generics.GenericAPIView):
    serializer_class = ManagerUserSerializer

    def get_queryset(self):
        return User.objects.filter(is_admin=True)

    def get(self, request, *args, **kwargs):
        data = self.list(request, *args, **kwargs)
        return Response({"result": "success", "message": None, "data": data})

    def post(self, request, *args, **kwargs):
        try:
            data = self.create(request, *args, **kwargs)
        except Exception as e:
            return Response({"result": "fail", "message": str(e), "data": None}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"result": "success", 'message': None, "data": data}, status=status.HTTP_201_CREATED)


class ManagerUserDetailView(mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            mixins.ListModelMixin,
                            generics.GenericAPIView):
    queryset = User.objects.filter(is_admin=True)
    serializer_class = ManagerUserSerializer

    def get(self, request, *args, **kwargs):
        try:
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
