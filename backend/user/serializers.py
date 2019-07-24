from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email
from django.utils import timezone
from rest_framework import serializers

from .models import CustomUser as User, Address


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'user_id', 'password', 'email', 'phone_number')
        validators = [

        ]
        extra_kwargs = {
            'password': {'write_only': True},
        }

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


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('address', 'user')

    def create(self, request):
        address = Address.objects.create(**request)
        address.save()
        return address
