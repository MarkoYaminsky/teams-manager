from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import (
    TeamCreateUpdateInputSerializer,
    TeamListOutputSerializer,
    TeamRetrieveCreateOutputSerializer,
    UserCreateUpdateInputSerializer,
    UserListOutputSerializer,
    UserRetrieveCreateOutputSerializer,
)
from users.services import (
    create_team,
    create_user,
    delete_team,
    delete_user,
    get_all_teams,
    get_all_users,
    update_team,
    update_user,
)


class UserListCreateApi(generics.ListAPIView):
    serializer_class = UserListOutputSerializer

    def get_queryset(self):
        return get_all_users()

    @extend_schema(request=UserCreateUpdateInputSerializer)
    def post(self, request, *args, **kwargs):
        serializer = UserCreateUpdateInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = create_user(**serializer.validated_data)
        return Response(UserRetrieveCreateOutputSerializer(user).data, status=status.HTTP_201_CREATED)


class UserRetrieveUpdateDestroyApi(APIView):
    serializer_class = UserRetrieveCreateOutputSerializer

    def get_object(self, user_id: str):
        return get_object_or_404(get_all_users(), id=user_id)

    def get(self, request, user_id):
        user = self.get_object(user_id)
        return Response(self.serializer_class(user).data, status=status.HTTP_200_OK)

    def patch(self, request, user_id):
        user = self.get_object(user_id)
        serializer = UserCreateUpdateInputSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        update_user(user, **serializer.validated_data)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, user_id):
        user = self.get_object(user_id)
        delete_user(user)
        return Response(status=status.HTTP_204_NO_CONTENT)


class TeamListCreateApi(generics.ListAPIView):
    serializer_class = TeamListOutputSerializer

    def get_queryset(self):
        return get_all_teams()

    @extend_schema(request=UserCreateUpdateInputSerializer)
    def post(self, request, *args, **kwargs):
        serializer = TeamCreateUpdateInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        team = create_team(**serializer.validated_data)
        return Response(TeamRetrieveCreateOutputSerializer(team).data, status=status.HTTP_201_CREATED)


class TeamRetrieveUpdateDestroyApi(APIView):
    serializer_class = TeamRetrieveCreateOutputSerializer

    def get_object(self, team_id: str):
        return get_object_or_404(get_all_teams(), id=team_id)

    def get(self, request, team_id):
        team = self.get_object(team_id)
        return Response(self.serializer_class(team).data, status=status.HTTP_200_OK)

    def patch(self, request, team_id):
        team = self.get_object(team_id)
        serializer = TeamCreateUpdateInputSerializer(team, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        update_team(team, **serializer.validated_data)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, team_id):
        team = self.get_object(team_id)
        delete_team(team)
        return Response(status=status.HTTP_204_NO_CONTENT)
