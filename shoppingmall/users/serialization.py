from rest_framework import serializers

from users.models import CustomUser as User


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "user_id", "password", "email")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return User(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get("user_id", instance.username)
        instance.user_id = validated_data.get("user_id", instance.user_id)
        instance.password = validated_data.get("user_id", instance.password)
        instance.email = validated_data.get("user_id", instance.email)
        instance.save()
        return instance


class UserLoginSerializer(serializers.Serializer):
    user_id = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        return user if user else serializers.ValidationError("fail login")


def authenticate(user_id=None, password=None):
    user = User.objects.filter(user_id=user_id, password=password)
    return user
