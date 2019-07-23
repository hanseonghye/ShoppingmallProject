from django.contrib.auth.password_validation import validate_password
from django.utils import timezone
from rest_framework import serializers
from user.models import CustomUser as User


class ManagerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'user_id', 'password')

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, request):
        user = User.objects.create(**request)
        user.set_password(request['password'])
        user.is_admin = True
        now = timezone.now()
        user.date_joined = now
        user.last_login = now
        user.save()
        return user
