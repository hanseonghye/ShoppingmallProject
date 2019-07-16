from rest_framework import viewsets, generics
from .serializers import UserSerializer
from .models import CustomUser as User


class UserViewSet(viewsets.ModelViewSet):
    # queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()

        return queryset

    # def list(self,request):
    #     pass
    #
    # def create(self, serializer):
    #     serializer.save(user=self.request.user)
