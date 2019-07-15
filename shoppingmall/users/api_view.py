from rest_framework import generics
from rest_framework.views import APIView
from users.models import CustomUser as User
from users.serialization import UserCreateSerializer


class Login(APIView):
    def post(self, request):
        user = User.is_authenticated
        # user = User(request.POST.get('id'), request.POST.get('passwprd'))


class RegistrationAPI(generics.GenericAPIView):
    serializer_class = UserCreateSerializer

    def post(self, request, *args, **kwargs):
        if len(request.)