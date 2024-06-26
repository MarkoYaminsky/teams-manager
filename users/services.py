from typing import Any

from django.contrib.auth import get_user_model
from django.db.models import Q, QuerySet

from common.services import update_instance

User = get_user_model()


def get_all_users(*args: Q, **kwargs: Any) -> QuerySet[User]:
    return User.objects.filter(*args, **kwargs)


def create_user(name: str, surname: str, email: str, password: str, **kwargs: Any) -> User:
    user = User.objects.create(name=name, surname=surname, email=email, **kwargs)
    user.set_password(password)
    user.save()
    return user


def update_user(user: User, **kwargs: Any) -> None:
    update_instance(instance=user, data=kwargs)


def delete_user(user: User) -> None:
    user.delete()
