from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication
from .models import CustomUser as User

class MyCustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        user_id = request.POST.get("user_id")
        password = request.POST.get("password")

        if not user_id or not password:
            return None

        try:
            user = User.objects.get(user_id=user_id, password=password)

        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return (user,None)