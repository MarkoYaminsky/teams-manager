import pytest
from django.contrib.auth import get_user_model
from django.db.models import Q

from users.models import Team
from users.services import (
    add_user_to_team,
    create_team,
    create_user,
    delete_team,
    delete_user,
    get_all_teams,
    get_all_users,
    remove_user_from_team,
    update_team,
    update_user,
)
from users.tests.factories import TeamFactory, UserFactory

User = get_user_model()

pytestmark = pytest.mark.django_db


class TestCreateUserService:
    name = "John"
    surname = "Doe"
    password = "password"
    email = "john.doe@example.com"

    def test_successful(self):
        team = TeamFactory()
        user = create_user(name=self.name, surname=self.surname, email=self.email, password=self.password, teams=[team])

        assert User.objects.count() == 1
        assert User.objects.first() == user
        assert user.teams.count() == 1
        assert user.teams.first() == team


class TestGetAllUsersService:
    name = "John"

    def test_with_kwargs(self):
        user = UserFactory(name=self.name)
        UserFactory(name="Eren", surname="Yeager")

        users = get_all_users(name=self.name)

        assert users.count() == 1
        assert users.first() == user

    def test_args(self):
        user = UserFactory(name=self.name)
        UserFactory(name="Eren", surname="Yeager")

        users = get_all_users(Q(name="John"))

        assert users.count() == 1
        assert users.first() == user

    def test_without_args(self):
        user_count = 2
        UserFactory.create_batch(size=user_count)

        users = get_all_users()

        assert users.count() == user_count


class TestUpdateUserService:
    new_name = "John"

    def test_successful(self):
        user = UserFactory(name="Not John")

        update_user(user=user, name=self.new_name)

        user.refresh_from_db()
        assert user.name == self.new_name


class TestDeleteUserService:
    def test_successful(self):
        user = UserFactory()
        not_deleted_user = UserFactory()

        delete_user(user)

        assert User.objects.count() == 1
        assert User.objects.first() == not_deleted_user


class TestCreateTeamService:
    name = "Survey Corps"

    def test_successful(self):
        team = create_team(name=self.name)

        assert Team.objects.count() == 1
        assert Team.objects.first() == team


class TestGetAllTeamsService:
    name = "Survey Corps"

    def test_success(self):
        team = TeamFactory(name=self.name)
        TeamFactory()

        teams = get_all_teams(name=self.name)

        assert teams.count() == 1
        assert teams.first() == team


class TestUpdateTeamService:
    new_name = "Survey Corps"

    def test_successful(self):
        team = UserFactory(name="Not Survey Corps")

        update_team(team=team, name=self.new_name)

        team.refresh_from_db()
        assert team.name == self.new_name


class TestDeleteTeamService:
    def test_successful(self):
        team = TeamFactory()
        not_deleted_team = TeamFactory()

        delete_team(team)

        assert Team.objects.count() == 1
        assert Team.objects.first() == not_deleted_team


class TestAddUserToTeamService:
    def test_successful(self):
        user = UserFactory()
        team = TeamFactory()

        add_user_to_team(user=user, team=team)

        assert team.people.count() == 1
        assert team.people.first() == user


class TestRemoveUserFromTeamService:
    def test_successful(self):
        user = UserFactory()
        team = TeamFactory()
        team.people.add(user)

        remove_user_from_team(user=user, team=team)

        assert team.people.count() == 0
        assert user not in team.people.all()
