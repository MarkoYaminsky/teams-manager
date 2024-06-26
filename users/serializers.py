from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from users.models import Team, User
from users.services import get_all_teams, get_all_users


class TeamShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ("id", "name")


class UserListOutputSerializer(serializers.ModelSerializer):
    teams = TeamShortSerializer(many=True)

    class Meta:
        model = User
        fields = (
            "id",
            "name",
            "surname",
            "email",
            "teams",
        )


class UserCreateInputSerializer(serializers.ModelSerializer):
    teams = serializers.ListSerializer(child=PrimaryKeyRelatedField(queryset=get_all_teams()), required=False)

    class Meta:
        model = User
        fields = ("name", "surname", "email", "password", "teams")


class UserUpdateInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("name", "surname", "email")


class UserRetrieveCreateOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "name", "surname", "email", "is_superuser", "is_staff")


class TeamListOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ("id", "name")


class TeamCreateInputSerializer(serializers.ModelSerializer):
    people = serializers.ListSerializer(child=PrimaryKeyRelatedField(queryset=get_all_users()), required=False)

    class Meta:
        model = Team
        fields = ("name", "people")


class TeamUpdateInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ("name",)


class UserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "full_name")


class TeamRetrieveCreateOutputSerializer(serializers.ModelSerializer):
    people = UserShortSerializer(many=True)

    class Meta:
        model = Team
        fields = ("id", "name", "people")
