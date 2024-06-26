import pytest
from django.contrib.auth import get_user_model
from django.db.models import Q

from users.services import create_user, delete_user, get_all_users, update_user
from users.tests.factories import UserFactory

User = get_user_model()

pytestmark = pytest.mark.django_db


class TestCreateUserService:
    name = "John"
    surname = "Doe"
    password = "password"
    email = "john.doe@example.com"

    def test_successful(self):
        user = create_user(name=self.name, surname=self.surname, email=self.email, password=self.password)

        assert User.objects.count() == 1
        assert User.objects.first() == user


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

        delete_user(user=user)

        assert User.objects.count() == 1
        assert User.objects.first() == not_deleted_user
