import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

from users.tests.factories import UserFactory

User = get_user_model()


@pytest.fixture
def user() -> User:
    return UserFactory()


@pytest.fixture
def api_client() -> APIClient:
    return APIClient()
