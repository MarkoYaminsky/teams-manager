from rest_framework import serializers

from users.models import Team, User


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


class TeamListOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ("id", "name")


class TeamCreateUpdateInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ("name",)


class TeamRetrieveCreateOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ("id", "name")
        # TODO When integrating with users, create an expanded version of team's users
