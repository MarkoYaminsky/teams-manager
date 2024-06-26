import pytest

from common.services import update_instance
from users.tests.factories import UserFactory

pytestmark = pytest.mark.django_db


class TestUpdateInstanceService:
    new_email = "hello@example.com"

    def test_no_fields(self):
        user = UserFactory()
        new_user_data = {"email": self.new_email}

        result = update_instance(data=new_user_data, instance=user)

        user.refresh_from_db()
        assert user.email == self.new_email
        assert result == (user, True)

    def test_with_fields(self):
        user = UserFactory()
        new_user_data = {"email": self.new_email, "dog": "Bullet"}

        update_instance(data=new_user_data, fields=("email",), instance=user)

        assert user.email == self.new_email

    def test_with_non_existent_fields(self):
        non_existent_field_name = "data"
        user = UserFactory()

        update_instance(data={non_existent_field_name: "non_existent"}, instance=user)

        assert getattr(user, non_existent_field_name, None) is None

    def test_no_changes(self, user):
        instance, is_updated = update_instance(data={"email": user.email}, instance=user)

        assert is_updated is False
        assert instance == user
