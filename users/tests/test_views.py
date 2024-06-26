import pytest
from django.urls import reverse
from rest_framework import status

from users.tests.factories import TeamFactory, UserFactory

pytestmark = pytest.mark.django_db


class TestUserListCreateApi:
    ROUTE = "users:user-list-create"

    def test_create(self, api_client, mocker):
        payload = dict(
            name="John",
            surname="Doe",
            email="john.doe@example.com",
            password="password",
        )
        user = UserFactory()
        create_user_mock = mocker.patch("users.views.create_user", return_value=user)

        response = api_client.post(reverse(self.ROUTE), data=payload)

        assert response.status_code == status.HTTP_201_CREATED
        assert response.json() == {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "surname": user.surname,
            "is_staff": False,
            "is_superuser": False,
        }
        create_user_mock.assert_called_with(**payload)

    def test_list(self, api_client, mocker):
        user = UserFactory()
        get_all_users_mock = mocker.patch("users.views.get_all_users", return_value=[user])

        response = api_client.get(reverse(self.ROUTE))

        assert response.status_code == status.HTTP_200_OK
        assert response.json()[0] == {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "surname": user.surname,
            "teams": [],
        }
        get_all_users_mock.assert_called_once_with()


class TestUserRetrieveUpdateDestroyApi:
    ROUTE = "users:user-retrieve-update-destroy"

    def test_retrieve(self, api_client):
        user = UserFactory()

        response = api_client.get(reverse(self.ROUTE, kwargs={"user_id": user.id}))

        assert response.status_code == status.HTTP_200_OK
        response_json = response.json()
        assert response_json["id"] == user.id
        assert "password" not in response_json

    def test_update(self, api_client, mocker):
        user = UserFactory()
        payload = dict(name="John")
        update_user_mock = mocker.patch("users.views.update_user")

        response = api_client.patch(reverse(self.ROUTE, kwargs={"user_id": user.id}), data=payload)

        assert response.status_code == status.HTTP_204_NO_CONTENT
        update_user_mock.assert_called_with(user, **payload)

    def test_delete(self, api_client, mocker):
        user = UserFactory()
        delete_user_mock = mocker.patch("users.views.delete_user")

        response = api_client.delete(reverse(self.ROUTE, kwargs={"user_id": user.id}))

        assert response.status_code == status.HTTP_204_NO_CONTENT
        delete_user_mock.assert_called_with(user)


class TestTeamListCreateApi:
    ROUTE = "users:team-list-create"

    def test_create(self, api_client, mocker):
        payload = dict(name="Survey Corps")
        team = TeamFactory()
        user = UserFactory()
        team.people.set([user])
        create_team_mock = mocker.patch("users.views.create_team", return_value=team)

        response = api_client.post(reverse(self.ROUTE), data=payload)

        assert response.status_code == status.HTTP_201_CREATED
        assert response.json() == {
            "id": team.id,
            "name": team.name,
            "people": [{"id": user.id, "full_name": user.full_name}],
        }
        create_team_mock.assert_called_with(**payload)

    def test_list(self, api_client, mocker):
        team = TeamFactory()
        get_all_teams_mock = mocker.patch("users.views.get_all_teams", return_value=[team])

        response = api_client.get(reverse(self.ROUTE))

        assert response.status_code == status.HTTP_200_OK
        assert response.json()[0] == {
            "id": team.id,
            "name": team.name,
        }
        get_all_teams_mock.assert_called_once_with()


class TestTeamRetrieveUpdateDestroyApi:
    ROUTE = "users:team-retrieve-update-destroy"

    def test_retrieve(self, api_client):
        team = TeamFactory()

        response = api_client.get(reverse(self.ROUTE, kwargs={"team_id": team.id}))

        assert response.status_code == status.HTTP_200_OK
        response_json = response.json()
        assert response_json["id"] == team.id

    def test_update(self, api_client, mocker):
        team = TeamFactory()
        payload = dict(name="Survey Corps")
        update_team_mock = mocker.patch("users.views.update_team")

        response = api_client.patch(reverse(self.ROUTE, kwargs={"team_id": team.id}), data=payload)

        assert response.status_code == status.HTTP_204_NO_CONTENT
        update_team_mock.assert_called_with(team, **payload)

    def test_delete(self, api_client, mocker):
        team = TeamFactory()
        delete_team_mock = mocker.patch("users.views.delete_team")

        response = api_client.delete(reverse(self.ROUTE, kwargs={"team_id": team.id}))

        assert response.status_code == status.HTTP_204_NO_CONTENT
        delete_team_mock.assert_called_with(team)


class TestMoveUserInTeamsApi:
    ROUTE = "users:move-user-in-teams"

    def test_post(self, api_client, mocker):
        user = UserFactory()
        team = TeamFactory()
        add_user_to_team_mock = mocker.patch("users.views.add_user_to_team")

        response = api_client.post(reverse(self.ROUTE, kwargs=dict(user_id=user.id, team_id=team.id)))

        assert response.status_code == status.HTTP_204_NO_CONTENT
        add_user_to_team_mock.assert_called_with(user=user, team=team)

    def test_delete(self, api_client, mocker):
        user = UserFactory()
        team = TeamFactory()
        add_user_to_team_mock = mocker.patch("users.views.remove_user_from_team")

        response = api_client.delete(reverse(self.ROUTE, kwargs=dict(user_id=user.id, team_id=team.id)))

        assert response.status_code == status.HTTP_204_NO_CONTENT
        add_user_to_team_mock.assert_called_with(user=user, team=team)
