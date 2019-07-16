from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email
from django.utils import timezone
from rest_framework import serializers

from .models import CustomUser as User


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    user_id = serializers.CharField()
    password = serializers.CharField()
    email = serializers.CharField()
    phone_number = serializers.CharField()
    date_joined = serializers.DateTimeField()

    class Meta:
        model = User
        fields = ('username', 'user_id', 'password', 'email', 'phone_number', 'date_joined')
        validators = [

        ]

    def validate_password(self, value):
        validate_password(value)
        return value

    def validate_email(self, value):
        validate_email(value)
        return value

    def create(self, request):
        user = User.objects.create(**request)
        now = timezone.now()
        user.set_password(request['password'])
        user.date_joined = now
        user.last_login = now
        user.save()
        return user
