from rest_framework import serializers

from users.models import User


class UserListOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "name",
            "surname",
            "email",
        )


class UserCreateUpdateInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("name", "surname", "email", "password")


class UserRetrieveCreateOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "name", "surname", "email", "is_superuser", "is_staff")
